from monitor import WebMonitor
import logging
import sys


if __name__ == '__main__':
    monitor = WebMonitor()
    monitor.start()
    try:
        user_input = input()
    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt to stop the running.")
        monitor.terminate()        # There is a 'endless WARNING:kafka.client:Unable to send to wakeup socket!' error when closing kafka.
                                   # Similar issue has been reported https://github.com/dpkp/kafka-python/issues/1842
                                   # will check that issue later.
        logging.info('WebMonitor ends.')
        sys.exit()
