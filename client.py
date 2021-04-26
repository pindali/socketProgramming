import socket

def main():
    cs = socket.socket()
    cs.connect(
        ("localhost",8081)
    )
    while True:
        
        print(cs.recv(1024).decode())
        data = input("enter msg for server : ")
        if data != "end":
            cs.send(bytes(data,"utf-8"))
        else:
            break
if __name__ == "__main__":
    main()