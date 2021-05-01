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
takenList =[]
class gui:
    def __init__(self,c):
        print("class object created")
        self.clientAddr = c
        self.isItmyturn = True
        self.clicked = False
        self.btnId = -1
        self.mainWindow = tkinter.Tk()
        self.button=[]
        self.msgFrame = tkinter.Frame(self.mainWindow)
        self.msgFrame.pack()
        self.msg = tkinter.Message( self.msgFrame, text = "Welcome to the game") 
        self.msg.pack(side ="top",fill ="both",expand=True)
        # self.matirx = [[-1]*3]*3
        self.matirx = [[0]*3 for _ in range(3)]

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
                self.msg['text'] = "You won the game!!"

                self.isItmyturn = True

                for dd in range(9):
                    takenList.append(dd+1)
                if s1 == 3:
                    for k in range(3):
                        print(i*3,end=" ")
                        print(k)
                        self.button[(i*3)+k]['bg'] = 'green'
                        
                if s2 == 3:
                    for k in range(3):
                        self.button[i+(3*k)]['bg']='green'
                return "m"
            if s1 == 30 or s2 ==30:
                self.msg['text'] = "You loss the game!!"

                self.isItmyturn = True

                for dd in range(9):
                    takenList.append(dd+1)
                if s1 == 30:
                    for k in range(3):
                        print(i*3,end=" ")
                        print(k)
                        self.button[(i*3)+k]['bg'] = 'red'
                        
                if s2 == 30:
                    for k in range(3):
                        self.button[i+(3*k)]['bg']='red'
                return "h"
        if md == 30 or od == 30:
            self.msg['text'] = "You loss the game!!"

            self.isItmyturn = True

            # for k in range(3):
            for dd in range(9):
                    takenList.append(dd+1)
            if md == 30:
                for dd in range(3):
                    for dd in range(3):
                        self.button[dd*4]['bg'] = 'red'
            if od == 30:
                for dd in range(3):
                    self.button[(dd+1)*2]['bg'] = 'red'

            return "h"
        if md == 3 or od ==3:
            self.msg['text'] = "You won the game!!"

            self.isItmyturn = True

            for dd in range(9):
                    takenList.append(dd+1)
            if md == 3:
                for dd in range(3):
                   self.button[dd*4]['bg'] = 'green'
            if od == 3:
                for dd in range(3):
                    self.button[(dd+1)*2]['bg'] = 'green'
            return "m"
        return "no one won!! lol"

    def AbleBtn(self):
        self.isItmyturn = True
        self.mainWindow.update()
                
    def clickBtn(self,id):
        self.clicked = True
        self.btnId = id
    def resetBtn(self):
        for b in self.button:
            b['text'] = ""
    def DisableBtn(self,id):
        if self.isItmyturn == True and id not in takenList:
            self.isItmyturn = False
            print(self.matirx)
            # print(self.checkWin())
            # print(self.isItmyturn)
            # print("btn clicked "+str(id))
            takenList.append(id)
            # print(id)
            print(self.checkWin())

            self.mainWindow.update()
            self.clientAddr.send(bytes(str(id),'utf-8'))
            self.button[id]['text'] = "X"
            self.mainWindow.update()
            self.matirx[index[id+1][0]-1][index[id+1][1]-1] = 1
            res = (self.checkWin())
            
            # print("wait for 10 sec")
            self.mainWindow.update()
            if res == "no one won!! lol":
                try:
                    cliVal = int(self.clientAddr.recv(1024).decode())
                    self.button[cliVal]['text'] = "O"
                    takenList.append(cliVal)
                    self.mainWindow.update()
                    self.matirx[index[cliVal+1][0]-1][index[cliVal+1][1]-1] = 10
                    print(self.checkWin())
                except:
                    pass

            self.AbleBtn()
            
    def main(self):
        self.mainWindow.title("TicTacToe")
        gameFrame = tkinter.Frame(self.mainWindow)
        gameFrame.pack(side= "bottom")
        # rest = tkinter.Button(msgFrame,width= 10,command= self.resetBtn)
        # rest.pack()
        for i in range(9):
            self.button.append(tkinter.Button(gameFrame,width=25,height=10,command= lambda id= i:self.DisableBtn(id),bg="#05f5e1"))
            self.button[i].grid(row=index[i+1][0],column=index[i+1][1])
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