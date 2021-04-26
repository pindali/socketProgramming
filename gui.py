import tkinter
import tkinter.font as font

import time
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
class gui:
    def __init__(self):
        print("class object created")
    
    

    def AbleBtn(self):
         for b in button:
            if b['state'] == tkinter.NORMAL:
                b['state']= tkinter.DISABLED
            else:
                b['state'] = tkinter.NORMAL

    def DisableBtn(self,id):
        # f = font.Font(size=10)
        button[id]['text'] = "X"
        button[id]['font'] = f
        print("wait for 10 sec")
        for b in button:
            if b['state'] == tkinter.NORMAL:
                b['state']= tkinter.DISABLED
            else:
                b['state'] = tkinter.NORMAL
        # time.sleep(10)   
        self.AbleBtn()
    def main(self):
        mainWindow = tkinter.Tk()
        mainWindow.title("TicTacToe")
        msgFrame = tkinter.Frame(mainWindow)
        msgFrame.pack()
        gameFrame = tkinter.Frame(mainWindow)
        gameFrame.pack(side= "bottom")

        msg = tkinter.Message( msgFrame, text = "Welcome to the game") 
        msg.pack(side ="top",fill ="both",expand=True) 
        for i in range(9):
            button.append(tkinter.Button(gameFrame,width=25,height=10,command= lambda id= i:self.DisableBtn(id),bg="darkgray"))
            button[i].grid(row=index[i+1][0],column=index[i+1][1])
        mainWindow.mainloop()
if __name__ =="__main__":
    g =gui()
    g.main()