import tkinter
import socket

index = {
    1:[1,1],
    2:[1,2],
    3:[1,3],
    4:[2,1],
    5:[2,2],
    6:[2,3],
    7:[3,1],
    8:[3,2],
    9:[3,3]
}
button=[]
takenList =[]
class gui:
    def __init__(self,c):
        print("class object created")
        self.clientAddr = c
        self.clicked = False
        self.btnId = -1
        self.mainWindow = tkinter.Tk()

    def AbleBtn(self):
         for b in range(len(button)):
            if b not in takenList:
                button[b]['state'] == tkinter.NORMAL
                
                
    def clickBtn(self,id):
        self.clicked = True
        self.btnId = id
    def DisableBtn(self,id):
        print("btn clicked "+str(id))
        if id not in takenList and button[id]['state'] != tkinter.DISABLED:
            takenList.append(id)
            print(id)
            self.mainWindow.update()
            self.clientAddr.send(bytes(str(id),'utf-8'))
            button[id]['text'] = "X"
            self.mainWindow.update()

            print("wait for 10 sec")
            for b in range(len(button)):
                if b not in takenList:
                    button[b]['state'] == tkinter.DISABLED
                    
            cliVal = int(self.clientAddr.recv(1024).decode())
            if cliVal not in takenList:
                button[cliVal]['text'] = "O"
                takenList.append(cliVal)
            self.AbleBtn()
        
    def main(self):
        self.mainWindow.title("TicTacToe")
        msgFrame = tkinter.Frame(self.mainWindow)
        msgFrame.pack()
        gameFrame = tkinter.Frame(self.mainWindow)
        gameFrame.pack(side= "bottom")

        msg = tkinter.Message( msgFrame, text = "Welcome to the game") 
        msg.pack(side ="top",fill ="both",expand=True) 
        for i in range(9):
            button.append(tkinter.Button(gameFrame,width=25,height=10,command= lambda id= i:self.DisableBtn(id),bg="#05f5e1"))
            button[i].grid(row=index[i+1][0],column=index[i+1][1])
        self.mainWindow.mainloop()

def main():
    s = socket.socket()
    s.bind(('localhost',8081))
    print("waiting for connection")
    s.listen(1)
    while True:
        c,addr = s.accept()
        print("connected to client")
        g = gui(c)
        g.main()
        c.close()
        break
if __name__ == "__main__":
    main()