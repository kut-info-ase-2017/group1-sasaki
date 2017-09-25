# -*- coding:utf-8 -*-

import socket
import dht12
import getch

host = "222.229.69.221" # サーバーのホスト名
port = 1234 # クライアントと同じPORT


serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインド
serversock.listen(10) # 接続の待ち受け (キューの最大数を指定)


def main():
    while True:
        print('Waiting for connections...')

        clientsock, client_address = serversock.accept() # 接続されればデータを格納

        msg = dht12.main()
        rcvmsg = clientsock.recv(1024)
        print('Received -> %s' % (rcvmsg))
        print('temperature: %d\n' % (msg))

        clientsock.sendall(msg.to_bytes(2, 'big')) # メッセージを返す

        clientsock.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' close')

