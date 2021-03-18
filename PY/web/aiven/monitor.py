# monitor 
# The main function to monitor the website(s), produce metrics, 
# stream the metrics to a kafka instance, and write the metrics to DB.


import logging
import pickle
import threading
import time
from checker import WebChecker
from config import WebMonConfig
from db import WebMonDB
from kafka import KafkaProducer, KafkaConsumer



class MonitorError(Exception):
    """Base exception for general web monitor error"""
    pass


class KafkaInitError(MonitorError):
    """Kafka initialization error"""
    pass


class WebMonitor(object):

    def __init__(self) -> None:
        self._web_checkers = []
        self._metrics_recorder = None
        self._producer = None
        self._consumer = None

        logging.basicConfig(level=logging.INFO)
        self._cfg = WebMonConfig().config()
        self._init_kafka()
        self._init_web_chekcers()
        self._init_metrics_recorder()

    def _init_kafka(self):
        assert self._cfg, 'self._cfg should not be empty'
        try:
            if self._producer:
                self._producer.close()
            self._producer = KafkaProducer(
                bootstrap_servers = self._cfg['kafka']['broker'],
                security_protocol = self._cfg['kafka']['sec_protocol'],
                ssl_cafile = self._cfg['kafka']["ssl_ca"],
                ssl_certfile = self._cfg['kafka']["ssl_cert"],
                ssl_keyfile = self._cfg['kafka']["ssl_key"],
                value_serializer = pickle.dumps,
                )
        except Exception as e:
            raise KafkaInitError(f'Failed to create kafka producer: {e}')

        try:
            self._consumer = KafkaConsumer(
                self._cfg['kafka']['topic'],
                bootstrap_servers = self._cfg['kafka']['broker'],
                security_protocol = self._cfg['kafka']['sec_protocol'],
                ssl_cafile = self._cfg['kafka']["ssl_ca"],
                ssl_certfile = self._cfg['kafka']["ssl_cert"],
                ssl_keyfile = self._cfg['kafka']["ssl_key"],
                value_deserializer = pickle.loads,
                )
        except Exception as e:
            logging.exception(e)
            raise KafkaInitError(f'Failed to create kafka consumer: {e}')

        
    def _init_web_chekcers(self) -> None:
        for wm in self._cfg['webmon']:
            url, pattern, intval = wm.values()
            chker = WebCheckTask(
                producer=self._producer, 
                topic=self._cfg['kafka']['topic'], 
                url=url, pattern=pattern, interval=int(intval))
            self._web_checkers.append(chker)

    def _init_metrics_recorder(self) -> None:
        db = WebMonDB()
        self._metrics_recorder = MetricsRecTask(consumer = self._consumer, db = db)

    def start(self) -> None:
        """Start all the website checking tasks"""
        if not self._web_checkers:
            self._init_web_chekcers()
        for chker in self._web_checkers:
            chker.start()
        if self._metrics_recorder:
            self._metrics_recorder.start()

    def terminate(self) -> None:
        """Stop all the website checking tasks"""
        for chker in self._web_checkers:
            chker.terminate()
        if self._metrics_recorder:
            self._metrics_recorder.terminate()


class WebCheckTask(threading.Thread):
    """The thread checking a specific website and produce metrics periodically"""

    def __init__(self, producer:KafkaProducer, topic:str,
                 url:str, pattern:str, interval:int=30) -> None:
        super().__init__()
        self._producer = producer
        self._topic = topic
        self._checker = WebChecker(url, pattern)
        self._interval = interval
        self._finish = False

    def run(self) -> None:
        while not self._finish:
            try:
                metrics = self._checker.check()
                self._producer.send(topic=self._topic, value=metrics)
                logging.info(f'Producer sending: {metrics}')
            except Exception as e:
                logging.exception(f'Web check task exception: {e}')
            time.sleep(self._interval)

    def terminate(self) -> None:
        self._finish = True
        logging.info(f'Terminate the web check task for {self._checker.url}')


class MetricsRecTask(threading.Thread):
    """The thread to check/record the metrics in kafka topics."""

    def __init__(self, consumer:KafkaConsumer, db:WebMonDB) -> None:
        super().__init__()
        self._consumer = consumer
        self._finish = False
        assert db, 'MetricsRecTask: Need a valid WebMonDB instance'
        self._db = db    # Only connect db when the task start running

    def run(self) -> None:
        if not self._db:
            self._db = db
        while not self._finish:
            try:
                if self._consumer:
                    self._consumer.poll()
                    for msg in self._consumer:
                        metrics = msg.value
                        logging.info(f'Consumer receiving: {metrics}')
                        self._db.write(metrics)
                        logging.info(f'Write to DB')
            except Exception as e:
                logging.exception(f'Metric record task exception {e}')
                raise e


    def terminate(self) -> None:
        self._finish = True
        logging.info('Terminate the metric record task.')
