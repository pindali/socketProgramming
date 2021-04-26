import socket
def chat(c):
    while True:
        data = input("send msg to client : ")
        if data != "end":
            c.send(bytes(data,"utf-8"))
            print(c.recv(1024).decode())
        else:
            return 
def main():
    s = socket.socket()
    s.bind(('localhost',8081))
    s.listen(1)
    while True:
        c,addr = s.accept()
        print("connected to client")
        chat(c)
        c.close()
        break
if __name__ == "__main__":
    main()