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
data = -1

cs = socket.socket()
class gui:
    def __init__(self,c):
        self.serverAddr = c
        self.mainWindow = tkinter.Tk()
        self.isItmyturn = False
        self.myMoves = []
        self.hisMoves = []
        self.button=[]
        self.matirx = [[0]*3 for _ in range(3)]
        # self.matirx = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    def AbleBtn(self):
        self.isItmyturn = True
        self.mainWindow.update()
    def checkWin(self):
        md = 0
        od = 0
        for i in range(3):
            s1 = 0
            s2 = 0
            for j in range(3):
                s1 = s1 + self.matirx[i][j]
                s2 = s2 + self.matirx[j][i]
                if i+j == 2:
                    od = od + self.matirx[i][j]
                if i == j :
                    md = md + self.matirx[i][j]
            if s1 == 3 or s2 == 3:
                if s1 == 3:
                    for k in range(3):
                        self.button[i+k]['bg'] = 'red'
                if s2 == 3:
                    for k in range(3):
                        self.button[i+(3*k)]['bg']='red'
                return "m"
            if s1 == 30 or s2 ==30:
                if s1 == 30:
                    for k in range(3):
                        self.button[i+k]['bg'] = 'red'
                if s2 == 30:
                    for k in range(3):
                        self.button[i+(3*k)]['bg']='red'
                return "h"
        if md == 30 or od == 30:
            return "h"
        if md == 3 or od ==3:
            return "m"
        return "no one won!! lol"

    def resetBtn(self):
        for b in self.button:
            b['text'] = ""
    def DisableBtn(self,id):
        if self.isItmyturn == True and id not in takenList:
            # print(id)
            # print(self.matirx)
            self.matirx[index[id+1][0]-1][index[id+1][1]-1] = 1
            # print(self.matirx)
            # print(self.checkWin())
            self.isItmyturn = False
            takenList.append(id)
            self.button[id]['text'] = "O"
            self.mainWindow.update()
            self.serverAddr.send(bytes(str(id),'utf-8'))
            self.mainWindow.update()
            print(self.checkWin())
            servVal = int(self.serverAddr.recv(1024).decode())
            self.hisMoves.append(servVal)
            takenList.append(servVal)
            self.button[servVal]['text'] = "X"
            self.mainWindow.update()
            self.matirx[index[servVal+1][0]-1][index[servVal+1][1]-1] = 10
            print(self.checkWin())
            
            self.AbleBtn()
    def main(self):
        self.mainWindow.title("TicTacToe")
        msgFrame = tkinter.Frame(self.mainWindow)
        msgFrame.pack()
        gameFrame = tkinter.Frame(self.mainWindow)
        gameFrame.pack(side= "bottom")
        # reset = tkinter.Button(msgFrame,width = 10, command= self.resetBtn)
        # reset.pack()
        msg = tkinter.Message( msgFrame, text = "Welcome to the game") 
        msg.pack(side ="top",fill ="both",expand=True) 
        for i in range(9):
            self.button.append(tkinter.Button(gameFrame,width=25,height=10,command= lambda id= i:self.DisableBtn(id),bg="darkgray"))
            self.button[i].grid(row=index[i+1][0],column=index[i+1][1])
        self.mainWindow.update()
        tmp  = int(cs.recv(1024).decode())
        self.button[tmp]['text'] = "X"
        takenList.append(tmp)
        self.isItmyturn = True
        self.mainWindow.update()
        self.matirx[index[tmp+1][0]-1][index[tmp+1][1]-1] = 10
        # print("the timer is compeleted")
        self.mainWindow.mainloop()

def main():
    
    cs.connect(
        ("localhost",8081)
    )
    g = gui(cs)
    g.main()

if __name__ == "__main__":
    main()