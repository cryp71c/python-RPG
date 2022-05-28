from audioop import add
from pydoc import cli
import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 44556              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

good = bytes("[*] File Hash Match", 'utf-8')
bad = bytes("[!] Check File Integrity", 'utf-8')
md5 = "1e5d173b89432a1f793ad1b4dbb50e88"
sha1 = "e35ca65f2cfced8ce9de6178e0a789e384e4f4c3"

try:
    while True:
        s.listen(1)
        conn, addr = s.accept()
        print(type(addr))
        print(f"Connection from: {addr[0]}:{addr[1]}")
        if bool(conn):
            conn.sendall(md5.encode('utf-8')) 
            conn.close()

except KeyboardInterrupt:
    print("\n[!] User Shutdown")
    quit()