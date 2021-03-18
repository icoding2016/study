from monitor import WebMonitor
import sys


if __name__ == '__main__':
    monitor = WebMonitor()
    monitor.start()
    try:
        user_input = input()
    except KeyboardInterrupt:
        monitor.terminate()
        sys.exit(0)
