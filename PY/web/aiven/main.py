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
        monitor.terminate()
        sys.exit(0)
