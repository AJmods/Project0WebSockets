import socket

HOST = "127.0.0.1"  # server IP address
PORT = 65432  # port number used by server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = input("Enter message")
    encodedMsg = str.encode(msg)
    s.sendall(encodedMsg)
    data = s.recv(1024)

decodedMSG = data.decode()
print(f"Received {decodedMSG}")
