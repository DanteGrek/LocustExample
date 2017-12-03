import socket
import pickle
import multiprocessing
import time


class ProcessMonitorClient(object):

    def __init__(self, host='localhost', port=9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.send('locust client')
        self.charts = {}

    def start_listening(self):
        try:
            while True:
                self.charts = pickle.loads(self.sock.recv(1024))
                print self.get_carts()
        except Exception:
            pass
        finally:
            self.close_connection()

    def launch_process_monitor_client(self):
        p = multiprocessing.Process(target=self.start_listening)
        p.start()
        print "Process monitor client started"

    def get_carts(self):
        return self.charts

    def close_connection(self):
        self.sock.close()


if __name__ == '__main__':
    process_monitor = ProcessMonitorClient()
    process_monitor.launch_process_monitor_client()
    time.sleep(3)
    print "GET CHARTS ", process_monitor.get_carts()
