import socket

HOST = "127.0.0.1"  # server host (127.0.0.1 is the same as localhost)
PORT = 65432  # Port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}");
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            newData = data.upper()  # make data uppercase
            conn.sendall(newData)  # send new data data
            print(f"sent {newData} to {addr}")
