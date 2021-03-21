import datetime
import time
import unittest
from checker import WebChecker
from db import WebMonDB
from kafka import KafkaProducer, KafkaConsumer
from monitor import WebMonitor
from unittest import mock



class UTest(unittest.TestCase):

    @mock.patch('checker.requests.get')
    def test_checker(self, mock1):
        url =  'http://kafka.apache.org/'
        pattern = r'<title>Apache\s*Kafka</title>'
        test_rsp = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
        <html xmlns:og="http://ogp.me/ns#">
	    <head>
		    <title>Apache Kafka</title>
		    <link rel='stylesheet' href='/css/styles.css?2' type='text/css'>
		    <link rel="icon" type="image/gif" href="/images/apache_feather.gif">
		    <meta name="robots" content="index,follow" />
        """
        chcker = WebChecker(url, pattern)
        mock_rsp = mock.Mock()
        mock_rsp.status_code = 200
        mock_rsp.text = test_rsp
        mock_rsp.elapsed = datetime.timedelta(microseconds=12345)
        mock1.return_value = mock_rsp
        result = chcker.check()
        self.assertTrue(result['success'])
        self.assertTrue(result['errcode'] == '200')
        self.assertTrue(result['rsptime'] == '0:00:00.012345')

    @mock.patch('db.psycopg2.connect')
    @mock.patch('monitor.KafkaConsumer')
    @mock.patch('monitor.KafkaProducer')
    def test_monitor(self, mock_pf, mock_cf, mock_df):
        url = 'http://kafka.apache.org/'
        mock_producer = mock.MagicMock()
        mock_producer.send.return_value = 0
        mock_consumer = mock.MagicMock()
        mock_consumer.poll.return_value = 0
        mock_consumer.__iter__.return_value.value = {
           'url':url,
           'success':True,
           'errcode':200,
           'rsptime':'0:00:00.012345'}
        mock_pf.return_value = mock_producer
        mock_cf.return_value = mock_consumer
        mock_conn = mock.MagicMock()
        mock_df.return_value = mock_conn
        monitor = WebMonitor()
        monitor.start()
        time.sleep(61)
        #mock_conn.execute.assert_called()
        mock_producer.send.assert_called()
        mock_consumer.__iter__.assert_called()

        # more tests ...

        monitor.terminate()

    # TODO: The test is incomplete...
    # more mock and non-mock test functions are needed for a better coverage.


if __name__ == '__main__':
    unittest.main()