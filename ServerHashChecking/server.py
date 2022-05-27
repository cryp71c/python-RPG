import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 44556              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

good = bytes("[*] File Hash Match", 'utf-8')
bad = bytes("[!] Check File Integrity", 'utf-8')

while 1:
    try:
        data = conn.recv(32).decode('utf-8')
        print(data)
        saved_hash = "feea33f22c73a2ded8830796fa6b4c68"

        if data != saved_hash:
            print(f"{conn} : {addr} : {data} : BAD HASH")
            conn.sendall(bad)
            
        else:
            print(f"{conn} : {addr} : {data} : GOOD HASH")
            conn.sendall(good)

    except ConnectionResetError:
        print("Client Disconnected.")
        break
    except BrokenPipeError:
        print("Broken Pipe.. dont know why")
        break

conn.close()
#s.shutdown(socket.SHUT_RDWR)
#s.close()