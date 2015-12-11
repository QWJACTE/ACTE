#!/usr/bin/python
# -*- encoding=utf-8 -*-

import socket
from handle import *

HOST = 'localhost'
PORT = 8080

def main():
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((HOST, PORT))
    ss.listen(5)

    while True:
        conn, addr = ss.accept()
        # record Client address
        log.get_log('Client addr', str(addr))

        try:
            conn.settimeout(50)
            buf = conn.recv(2048)
            back_msg = handle.handle(buf)
            if back_msg[0] == const.ILLEGAL_REQUEST:
                raise ILLEGAL_REQUEST_EXCEPTION
            else:
                conn.sendall(back_msg[1])
        except socket.timeout:
            print 'time out'
        except ILLEGAL_REQUEST_EXCEPTION:
            conn.sendall(const.ILLEGAL_REQUEST)
        conn.close()

    ss.close()

if __name__ == '__main__':
    main()