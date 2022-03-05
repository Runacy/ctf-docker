"""
reference
https://engineeringnote.hateblo.jp/entry/python/bhp/3-3

pythonでIPのデコードをする場合は、structsを使うと簡単にできるらしい。

os.name == posix

使うときは別のterminalか開いて、pingを送信したりして使う。
"""

import socket
import struct
from ctypes import *

class IP(Structure): # Structureを継承
    """
    cの構造体を呼べるけど実体も紐づいてるってことなんかねこれ多分そうなんかな。
    構造体と共用体
構造体と共用体は ctypes モジュールに定義されている Structure および Union ベースクラスからの派生クラスでなければなりません。
それぞれのサブクラスは _fields_ 属性を定義する必要があります。 
_fields_ は フィールド名 と フィールド型 を持つ 2要素タプル のリストでなければなりません。
    """
    _fields_ = [
        ("version",       c_uint8, 4), # バージョン(4)
        ("ihl",           c_uint8, 4), # ヘッダ長(4)
        ("tos",           c_uint8),  # サービスタイプ
        ("len",           c_uint16), # 全長
        ("id",            c_uint16), # 識別子
        ("offset",        c_uint16), # フラグメントオフセット
        ("ttl",           c_uint8), # パケット生存時間
        ("protocol_num",  c_uint8), # プロトコル番号
        ("sum",           c_uint16), # チェックサム
        ("src",           c_uint32), # 発信元アドレス
        ("dst",           c_uint32) # 宛先アドレス
    ]
 
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
 
    def __init__(self, socket_buffer=None):
        self.protocol_map = {1: "ICMP", 6:"TCP", 17:"UDP"}
        """
        <:  リトルエンディアン standard none

        ネイティブのバイトオーダはビッグエンディアンかリトルエンディアンで、ホスト計算機に依存します。
        例えば、Intel x86 および AMD64 (x86-64) はリトルエンディアンです。

        L:  unsigned long 整数

        struct.pack バイナリを返す
        """
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src)) #発信元アドレス
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst)) #痩身元アドレス
 
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

def main(host):
  
  socket_protocol = socket.IPPROTO_ICMP # pプロトコル番号。番号でも可能

  sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

  sniffer.bind((host, 0))
  """
  https://linuxjm.osdn.jp/html/LDP_man-pages/man7/raw.7.html
  socket.IP_HDRINCLを有効化
  raw ソケットは、リンクレベルヘッダーを 含まない raw データグラムの送受信ができる
  """

  print("socket.IPPROTO_IP=> ", socket.IPPROTO_IP)
  print("socket.IP_HDRINCL=> ", socket.IP_HDRINCL)
  sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)


  while True:
    raw_buffer = sniffer.recvfrom(65565)[0]
    ip_header = IP(raw_buffer[0:20])

    print("Protocol: {} {} -> {} TTL: {}".format(ip_header.protocol, ip_header.src_address,
                                            ip_header.dst_address, ip_header.ttl))


if __name__ == "__main__":
  main(host="127.0.0.1")