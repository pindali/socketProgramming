import tkinter
import time
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
takenList = []
button=[]
data = -1
cs = socket.socket()
class gui:
    def __init__(self,c):
        self.serverAddr = c
        self.mainWindow = tkinter.Tk()
    def AbleBtn(self):
        for b in range(len(button)):
                if b not in takenList:
                    button[b]['state'] == tkinter.NORMAL
                    

    def DisableBtn(self,id):
        print("btn clicked "+str(id))
        if id not in takenList and button[id]['state'] != tkinter.DISABLED:
            print(id)
            takenList.append(id)
            button[id]['text'] = "O"
            self.mainWindow.update()
            self.serverAddr.send(bytes(str(id),'utf-8'))
            for b in range(len(button)):
                    if b not in takenList:
                        button[b]['state'] == tkinter.DISABLED
                
            servVal = int(self.serverAddr.recv(1024).decode())
            if servVal not in takenList:
                takenList.append(servVal)
                button[servVal]['text'] = "X"
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
            button.append(tkinter.Button(gameFrame,width=25,height=10,command= lambda id= i:self.DisableBtn(id),bg="darkgray"))
            button[i].grid(row=index[i+1][0],column=index[i+1][1])
        self.mainWindow.update()
        tmp  = int(cs.recv(1024).decode())
        button[tmp]['text'] = "X"
        takenList.append(tmp)
        self.mainWindow.update()

        print("the timer is compeleted")
        self.mainWindow.mainloop()

def main():
    
    cs.connect(
        ("localhost",8081)
    )
    g = gui(cs)
    g.main()

if __name__ == "__main__":
    main()