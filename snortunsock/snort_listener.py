import os
import socket

import alert

BUFSIZE = alert.AlertPkt._ALERTPKT_SIZE
SOCKFILE = "/tmp/snort_alert"


def start_recv():
    '''Open a server on Unix Domain Socket'''
    if os.path.exists(SOCKFILE):
        os.unlink(SOCKFILE)
    unsock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    unsock.bind(SOCKFILE)
    print("Unix socket start listening...")
    i = 0
    while True:
        i += 1
        data = unsock.recv(BUFSIZE)
        parsed_msg = alert.AlertPkt.parser(data)
        if parsed_msg:
            yield parsed_msg

if __name__ == '__main__':
    start_recv()