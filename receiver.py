import socket
import datetime

backlog = 5
size = 100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 30000))
s.listen(backlog)

last_packet = None
bit = ''
while 1:

    client, address = s.accept()
    data = client.recv(size)

    current_time = datetime.datetime.now()

    if last_packet is not None:

        my_delta = (current_time - last_packet)
        microseconds = my_delta.microseconds + my_delta.seconds * 1000000

        possible_zeros = round(microseconds / 300000)

        if possible_zeros > 0:
            bit += possible_zeros * '0'
            bit += '1'
        else:
            bit += '1'

        print(microseconds, my_delta.seconds, bit[:len(bit)-1])

    last_packet = current_time