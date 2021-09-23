
import socket
import time


host = '192.168.1.113'  # '127.0.0.1'
port = 6666
unix_sock = "/var/run/test.socket"
# peer server could be another python app (socket server listion on port) or
# sudo nc -U /var/run/test.socket -l
# sudo nc -p 6666 -l
#  

def client():
    # Address Family:AF_INET (used for Internet inter-process communication) or 
    #                AF_UNIX (used for inter-process communication on the same machine)
    # Type: SOCKET_STREAM (stream socket, mainly used for TCP protocol) Or 
    #       SOCKET_DGRAM (datagram socket, mainly used for UDP protocol)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as sock:
        sock.connect((host, port))    # socket.AF_INET
        # sock.connect(unix_sock)
        print(f"Create socket {sock}")

        print("sending...")
        try:
            for i in range(10):
                data = str(i)+'\n'
                sock.sendall(data.encode('utf-8'))
                time.sleep(0.5)
            print("Done.")
        except:
            raise
        finally:
            sock.close()
            print("socket closed")


client()
