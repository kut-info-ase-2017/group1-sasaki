# -*- coding:utf-8 -*-
import socket

host = "222.229.69.221" # サーバーのホスト名
port = 1234 # PORTを指定

def temperture():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # オブジェクトの作成

    try:
        client.connect((host, port)) # サーバーに接続
    except ConnectionRefusedError:
        print('\n')
        print('temperature: Unable to get the temperature')
        return 20 # 季節の判定に影響のない値を返す

    client.send(b"ok") # データを送信

    response = client.recv(4096) # レシーブ (２進数)

    temp = int.from_bytes(response, 'big')

    print('\n')
    print('temperature: %d' % temp)

    return temp
