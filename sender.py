import time
import socket

__author__ = 'Eduardo J Castillo'
__email__ = 'castilloej@email.wofford.edu'


class CovertChannel:

    def __init__(self, destination, port):

        self._ip = destination
        self._port = port
        self._message = ''
        self._interval = 0.3

    def AddToMessage(self, a_bit):

        self._message += a_bit

    def SendMessage(self):

        time.sleep(self._interval)

        for bit in '1' + self._message + '1':

            if bit == '1':
                self._send_packet()
            else:
                time.sleep(self._interval)

    def _send_packet(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((self._ip, self._port))
        s.send(bytes('-', 'UTF-8'))
        s.close()


MyCovert = CovertChannel('201.211.236.187', 30000)

Message = input('Give me bits:')

MyCovert.AddToMessage(Message)
MyCovert.SendMessage()