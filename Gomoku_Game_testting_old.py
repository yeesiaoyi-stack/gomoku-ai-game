#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import messagebox
from abc import *
import random #machine
import math #machine

Player1 = ""
Player2= ""

if Player1
window1 = tk.Tk()
window1.title("Gomoku")
window1.configure(bg="SandyBrown")
class Player(ABC):
    @abstractmethod
    def name(self):
        pass

class Player1(Player):
    def name(self):
        player1 = tk.Label(window1,text = "Player 1's name : ",font=("arial",12),bg="SandyBrown").grid(column=2,row=3)
        name1 = tk.Entry(window1,text=player11,font=("arial",12)).grid(column=4,row=3)
        return player11
class Player2(Player):
    def name(self):
        player2 = tk.Label(window1,text = "Player 2's name : ",font=("arial",12),bg="SandyBrown").grid(column=2,row=4)
        name2 = tk.Entry(window1,text=player22,font=("arial",12)).grid(column=4,row=4)
        return player22
        
class Main1:
    def display(self):
        k=Player1().name()
        b=Player2().name()
        window2 = tk.Toplevel()
        window2.title("Gomoku")
        window2.configure(bg="SandyBrown")
        dis = tk.Label(window2,text = "Hello, "+k.get()+". Your piece color is black color.",font=("arial",12),bg="SandyBrown")
        dis.grid(column=2,row=6)
        dis2 =tk.Label(window2,text = "You should start first",font=("arial",12),bg="SandyBrown")
        dis2.grid(column=2,row=7)
        dis1 = tk.Label(window2,text = "Hello, "+b.get()+". Your piece color is white color.",font=("arial",12),bg="SandyBrown")
        dis1.grid(column=2,row=8)
        dis3 =tk.Label(window2,text = "You need to wait for the player 1 to place the pieces first",font=("arial",12),bg="SandyBrown")
        dis3.grid(column=2,row=9)
        btn4 = tk.Button(window2, text="Confirm",command = lambda: Application(master = tk.Toplevel()),font=("arial",12))
        btn4.grid(column=2,row=11)
        window2.mainloop()


        
    
welcome = tk.Label(window1,text = "Welcome to play Gomoku Game ^^",font=("arial",12),bg="SandyBrown").grid(column=3,row=1)
inputName = tk.Label(window1,text = "Please enter your name",font=("arial",12),bg="SandyBrown").grid(column=2,row=2)
player11 = tk.StringVar()
player22 = tk.StringVar()
Player1().name()
Player2().name()

     
k = Main1()
btn2 = tk.Button(window1, text="Enter",command = lambda:k.display(),font=("arial",12)).grid(column=3,row=6)
#Set the parameters
r = 10
click_x=0                 #Define the x-axis coordinates
click_y=0                 #Define the y-axis coordinates
piece_color ="black"    #current piece color
person_flag = 1           #-1 = white color，1 = black color
a_flag = 1                #Cannot click on the board when one side wins
mouse_black = []          #black piece's coordinate storage list
mouse_white = []          #white piece's coordinate storage list
mouse = []                #all piece's coordinate storage list
totala=0
totalb=0
ret=1
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        master.title("Gomoku")
        
        canvas = tk.Canvas(master,bg= "SandyBrown", width = 480, height = 480)
        canvas.grid(row = 0, column = 0, rowspan = 10)
        for i in range(15):
            canvas.create_line(30, (30 * i + 30), 450, (30 * i + 30)) #Show 15 horizontal lines
            canvas.create_line((30* i + 30), 30, (30 * i + 30), 450) #show 15 vertical lines

        point_x = [3, 3, 11, 11, 7]
        point_y = [3, 11, 3, 11, 7]
        for i in range(5):
            canvas.create_oval(30 * point_x[i] + 27, 30 * point_y[i] + 27,
                               30 * point_x[i] + 33, 30 * point_y[i] + 33, fill = "black") #show 5 titik bulat


        class MouseJudge:
            def mouseJudge(self):
                global click_x, click_y, person_flag, mouse, piece_color
                pu = Put()
                mouse = mouse_black + mouse_white   #Store all the coordinates of chess pieces (black and white)
                i=0
                j=0

                while click_x > (30+15*i):     #Determine the grid where the mouse click position is located
                    i+=1
                while click_y > (30+15*j):
                    j+=1
                if ((i%2)==1 and (j%2)==1):      #Divide a grid into four areas, and divide the vertices of the grid
                    click_x=30+15*(i-1)          #according to the area where the mouse clicks.                 
                    click_y=30+15*(j-1)                            
                if ((i%2)==1 and (j%2)==0):
                    click_x=30+15*(i-1)
                    click_y=30+15*j
                if ((i%2)==0 and (j%2)==1):
                    click_x=30+15*i
                    click_y=30+15*(j-1)
                if ((i%2)==0 and (j%2)==0):
                    click_x=30+15*i
                    click_y=30+15*j
                if person_flag ==1:
                    pu.putPiece("black")
                elif person_flag ==-1:
                    pu.putPiece("white")

        class Put:           
            #put piece  
            def putPiece(self,piece_color):
                global mouse_black, mouse_white, person_flag, mouse,ret
                Ju = J()
                S = Turn()
                W = WinTips()
                ret=1
                if (click_x>=30)and(click_x<=450)and(click_y>=30)and(click_y<=450): #Pieces can only be generated within checkerboard
                    if (click_x, click_y) not in mouse:   #One point can only produce one piece
                        if a_flag == 0:
                            canvas.create_oval(click_x - r, click_y - r,
                                               click_x + r, click_y + r,
                                               fill = piece_color, tags = ("piece"))
                            person_flag *= -1
                            if piece_color == "white":
                                S.Show(mouse)
                                mouse_white.append( (click_x, click_y) )   #Put the white piece coordinates
                                Ju.Judge1(mouse_white)
                                W.Tips(mouse)
                            elif piece_color == "black":
                                S.Show(mouse)
                                mouse_black.append( (click_x, click_y) )   #Put the black piece coordinates
                                Ju.Judge1(mouse_black)
                                W.Tips(mouse)       
                        else:
                            return 0

        #Judge winning or losing based on the number of consecutive pieces
        class Win:
            def pieceCount(self,mouse,pieces_count,p,q):
                global piece_count
                if person_flag==-1:   #judge black piece
                    for i in range(1,5):
                        (x, y) = (click_x + p * 30 * i, click_y + q * 30 * i)
                        if (x, y) in mouse_black:
                            piece_count+=1
                        else:
                            break
                    return piece_count
                if person_flag==1:   #judge white piece
                    for i in range(1,5):
                        (x, y) = (click_x + p * 30 * i, click_y + q * 30 * i)
                        if (x, y) in mouse_white:
                            piece_count+=1
                        else:
                            break
                    return piece_count
        class J:
            #Judge winning or losing from three directions: horizontal, vertical and oblique
            def Judge1(self,mouse):
                global piece_count, piece_color
                piece_count = 0
                piece_count = Win().pieceCount(mouse,piece_count,-1,0)              #Judging from the coordinates of the drop point to the left
                piece_count = Win().pieceCount(mouse,piece_count,1,0)               #Judging from the coordinates of the drop point to the right

                if  piece_count == 4:
                    return 5
              
                else:
                    piece_count = 0
                    piece_count = Win().pieceCount(mouse,piece_count,0,-1)          #Judging from the coordinates of the drop point to the upwards
                    piece_count = Win().pieceCount(mouse,piece_count,0,1)           #Judging from the coordinates of the drop point to the downwards
                    if piece_count == 4:
                        return 5
                    
                    else:
                        piece_count = 0
                        piece_count = Win().pieceCount(mouse,piece_count,-1,-1)     #Judging from the coordinates of the drop point to the upper left corner
                        piece_count = Win().pieceCount(mouse,piece_count,1,1)       #Judging from the coordinates of the drop point to the lower right corner
                        if piece_count == 4:
                            return 5
                   
                        else:
                            piece_count = 0
                            piece_count = Win().pieceCount(mouse,piece_count,1,-1)  #Judging from the coordinates of the drop point to the upper right corner
                            piece_count = Win().pieceCount(mouse,piece_count,-1,1)  #Judging from the coordinates of the drop point to the lower left corner
                            if piece_count == 4:
                                return 5
                          
                            else:
                                return 0
        #Indicate which player's turn it is
        class Turn:
            def Show(self,mouse):
                var1 = tk.StringVar()
                if person_flag==1:
                    piece_canvas = tk.Canvas(master, width = 200, height = 50)
                    piece_canvas.grid(row = 0, column = 1)
                    piece_canvas.create_oval(100 - r, 30 - r,
                                            100 + r, 30 + r,
                                            fill = 'black')
                    var1.set("Player 1(black)'s Turn")
                    label = tk.Label(master, textvariable=var1, font=("arial",16))
                    label.grid(row = 1,column = 1)
                if person_flag==-1:
                    piece_canvas = tk.Canvas(master, width = 200, height = 50)
                    piece_canvas.grid(row = 0, column = 1)
                    piece_canvas.create_oval(100 - r, 30 - r,
                                            100 + r, 30 + r,
                                            fill = 'white')
                    var1.set("Player 2(white)'s Turn")
                    label = tk.Label(master, textvariable=var1, font=("arial",16))
                    label.grid(row = 1,column = 1)

        #Win Tips
        class WinTips:
            def Tips(self,mouse):
                Ju = J()
                var2 = tk.StringVar()
                var9 = tk.StringVar()
                global a_flag,totala,totalb
                if totala == 5 or totalb == 5:
                    if totala == 5:
                        var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                        var9.set("        Player 1(black) Win        ")
                        label = tk.Label(master, textvariable=var2, font=("arial",17))
                        label.grid(row = 1,column = 1)
                        label = tk.Label(master, textvariable=var9, font=("arial",17))
                        label.grid(row = 2,column = 1) 
                        a_flag = 1
                        return a_flag
                        
                    elif totalb == 5:
                        var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                        var9.set("        Player 2(white) Win        ")
                        label = tk.Label(master, textvariable=var2, font=("arial",17))
                        label.grid(row = 1,column = 1)
                        label = tk.Label(master, textvariable=var9, font=("arial",17))
                        label.grid(row = 2,column = 1) 
                        a_flag = 1 
                        return a_flag
                    else:
                        var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                        var9.set("            Draw Game            ")
                        label = tk.Label(master, textvariable=var2, font=("arial",17))
                        label.grid(row = 1,column = 1)
                        label = tk.Label(master, textvariable=var9, font=("arial",17))
                        label.grid(row = 2,column = 1) 
                        a_flag = 1
                        return a_flag
                if  person_flag==-1:
                    totala+=Ju.Judge1(mouse)
                    var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                    label = tk.Label(master, textvariable=var2, font=("arial",14))
                    label.grid(row = 2,column = 1)
                    #a_flag = 1
                    return a_flag
                if  person_flag==1:
                    totalb+=Ju.Judge1(mouse)
                    var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                    label = tk.Label(master, textvariable=var2, font=("arial",14))
                    label.grid(row = 2,column = 1)
                    #a_flag = 1
                    return a_flag   


        # After restarting, the loser plays first
        class Reset:
            def click_reset(self):
                var3 = tk.StringVar()
                global a_flag, mouse_black, mouse_white, mouse,totala,totalb,person_flag
                canvas.delete("piece")
                mouse_black = []
                mouse_white = []
                mouse = []
                a_flag=0
                person_flag=1
                totala,totalb=0,0
                piece_color = "black"
                var3.set("                                               ")
                label = tk.Label(master, textvariable=var3, font=("arial",16))
                label.grid(row = 2,column = 1)
                piece_canvas = tk.Canvas(master, width = 200, height = 50)
                piece_canvas.grid(row = 0, column = 1)
                piece_canvas.create_oval(100 - r, 30 - r,100 + r, 30 + r,fill = 'black')
                var.set("             Player 1's(black) Turn            ")
                label = tk.Label(master, textvariable=var, font=("arial",16))
                label.grid(row = 1,column = 1)
                

        #regret chess
        class Return:
            def click_return(self):
                global mouse,person_flag,totala,totalb,ret, mouse_black,mouse_white
                Ju = J()
                if ret==0:
                    return
                canvas.delete("piece")
                ret=0
                var2 = tk.StringVar()
                if person_flag==-1:
                    try:
                        mouse_black.pop()
                        mouse=mouse_black+mouse_white
                        totala-=Ju.Judge1(mouse)
                        var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                        label = tk.Label(master, textvariable=var2, font=("arial",14))
                        label.grid(row = 2,column = 1)
                        for i in range(len(mouse_black)):
                            canvas.create_oval(mouse_black[i][0]-r,mouse_black[i][1]-r
                                              ,mouse_black[i][0]+r,mouse_black[i][1]+r,fill="black",tags="piece")
                        for i in range(len(mouse_white)):
                            canvas.create_oval(mouse_white[i][0]-r,mouse_white[i][1]-r
                                              ,mouse_white[i][0]+r,mouse_white[i][1]+r,fill="white",tags="piece")
                        
                    except IndexError:
                        messagebox.showinfo("Information","There are no more white pieces on the checkerboard.",parent=master)
                        return 0
                    
                    
                if person_flag==1: 
                    try:
                        mouse_white.pop()
                        mouse=mouse_black+mouse_white
                        totalb-=Ju.Judge1(mouse)
                        var2.set("Player 1(black)%s:%sPlayer 2(white)"%(totala,totalb))
                        label = tk.Label(master, textvariable=var2, font=("arial",14))
                        label.grid(row = 2,column = 1)
                        for i in range(len(mouse_black)):
                                canvas.create_oval(mouse_black[i][0]-r,mouse_black[i][1]-r
                                                  ,mouse_black[i][0]+r,mouse_black[i][1]+r,fill="black",tags="piece")
                        for i in range(len(mouse_white)):
                            canvas.create_oval(mouse_white[i][0]-r,mouse_white[i][1]-r
                                             ,mouse_white[i][0]+r,mouse_white[i][1]+r,fill="white",tags="piece")
                 
                    except IndexError:
                            messagebox.showinfo("Information","There are no more black pieces on the checkerboard.",parent=master)
                            return 0
                    
                person_flag *= -1
                S = Turn()
                S.Show(mouse)

                    
                    

                
        class Mouse:    
        #Click the left button to return to the current position 
            def mouseBack(self,event):    
                global click_x, click_y
                click_x = event.x
                click_y = event.y
                moj = MouseJudge()
                moj.mouseJudge()
        m = Mouse().mouseBack
        canvas.bind("<Button-1>",m)

        class Scrollbar:
            def ins(self):
                self.window3 = tk.Tk()
                self.window3.title("instruction")
                self.inner_frame = tk.Frame(self.window3)
                self.inner_frame.pack()

                self.listbox = tk.Listbox(self.inner_frame,height=5,width=50)
                self.listbox.pack(side='left')
                self.v_scrollbar = tk.Scrollbar(self.inner_frame, orient=tk.VERTICAL)
                self.v_scrollbar.pack(side='right',fill=tk.Y)
                self.h_scrollbar = tk.Scrollbar(self.window3, orient=tk.HORIZONTAL)
                self.h_scrollbar.pack(side='bottom',fill=tk.X)
                self.v_scrollbar.config(command=self.listbox.yview)
                self.h_scrollbar.config(command=self.listbox.xview)
                self.listbox.config(yscrollcommand=self.v_scrollbar.set,
                                    xscrollcommand=self.h_scrollbar.set)

                data = [
                        "1. The player with the black pieces starts first",
                        "2. Place the pieces on the board",
                        "3. The first person to connect to five points wins"
                        ]

                for element in data:
                    self.listbox.insert(tk.END,element)
                    
                self.window3.mainloop()




        re=Reset()
        rr=Return()

        button1 = tk.Button(master,text="Start/Restart",font=('bold', 10),fg='blue',width=10,height=2,command=lambda:re.click_reset())
        button1.grid(row = 3,column = 1)
        button2 = tk.Button(master,text="Undo",font=('bold', 10),fg='red',width=10,height=2,command=lambda:rr.click_return())
        button2.grid(row = 5,column = 1)
        i = Scrollbar()
        button3 = tk.Button(master,text="Instruction",font=('bold',10),fg='black',width=10,height=2,command=lambda:i.ins())
        button3.grid(row = 7,column = 1)
        button4 = tk.Button(master,text="Exit",font=('bold',10),fg='black',width=10,height=2,command=lambda:window1.destroy())
        button4.grid(row = 9,column = 1)
        var = tk.StringVar()

        piece_canvas = tk.Canvas(master, width = 200, height = 50)
        piece_canvas.grid(row = 0, column = 1)
        piece_canvas.create_oval(100 - r, 30 - r,100 + r, 30 + r,fill = 'black')
        var.set("Player 1's(black) Turn")
        label = tk.Label(master, textvariable=var, font=("arial",16))
        label.grid(row = 1,column = 1)


        self.master.mainloop()



window1.mainloop()


# In[ ]:





# In[5]:





# In[ ]:




