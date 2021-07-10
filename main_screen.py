from tkinter import *  
from tkinter.ttk import *
from PIL import ImageTk,Image

selectedPlayer = 2

def mainScreen():
    def playerSelected(event):
        global selectedPlayer
        print("called")
        selectedPlayer=noOfPlayers.get()


    def gameStart():
        global selectedPlayer
        root.destroy()

    #selectedPlayer = 2
    root = Tk()     
    root.geometry('800x800')
    root.resizable(False, False)
    root.title('Chain Reaction')
    values=(2,3,4)


    bgImageFrame = Frame(root, relief='raised', borderwidth=2)
    bgImageFrame.pack(fill=BOTH, expand=YES)
    bgImageFrame.pack_propagate(False)

    img = ImageTk.PhotoImage(Image.open("mainMenu.jpg"))  
    mainImage=Label(bgImageFrame,image=img)
    mainImage.pack() 

    playerSelectionFrame = Frame(bgImageFrame, relief='raised', borderwidth=2)
    playerSelectionFrame.place(x=290, y=500)

    noOfPlayers=Combobox(playerSelectionFrame) 
    noOfPlayers['values']=(2,3,4)
    noOfPlayers['state'] = 'readonly'
    noOfPlayers.current(0)
    noOfPlayers.pack(side="right")
    noOfPlayers.bind('<<ComboboxSelected>>', playerSelected)

    text=Label(playerSelectionFrame,text="No of Players: ")
    text.pack(side="left")

    startButtonFrame=Frame(bgImageFrame,relief="raised",borderwidth=2)
    startButtonFrame.place(x=360,y=550)
    startBtn=Button(startButtonFrame,text="start",command=gameStart)
    # startBtn.bind("<Button-1>",gameStart)
    startBtn.pack()
    root.mainloop()
    return selectedPlayer

if __name__=="__main__":
    ret=mainScreen()
    print("from main loop",ret)

