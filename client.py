from grid import Grid
import tkinter as tk
from tkinter import Frame, ttk
from network import *
from _thread import *

def call_join(root, local_page,  widget_destroy, image_frame, grid_size, button_style):
       
    # player_number, grid_size = int(player_number) + 1, int(grid_size)
    # print(f'No. of Player: {player_number-1}\nGrid Size: {grid_size}')

    # def newgame_function():
    #     widget_destroy(root)
    #     call_join(root, mainScreen, widget_destroy, home_page, image_frame,
    #               player_number - 1, grid_size, button_style)

    # def back_function():
    #     mainScreen(root, home_page, image_frame, button_style)
    
    widget_destroy(root)
    image_frame()
    
    
    ip_label = ttk.Label(root, text="IP Address:")
    ip_label.place(x= 300-50, y = 500)
        
    ipaddress = tk.StringVar()
    ipaddress.set("192.168.000.000")
    ip_entry = ttk.Entry(root, textvariable = ipaddress, width=15)
    ip_entry.place(x= 350, y = 500)
    

    
    submit_button = ttk.Button(root, text="Submit", style='W.TButton', command= local_page)
    submit_button.place(x= 300, y = 520)

    
    back_button = ttk.Button(root, text='Back', style = "W.TButton", command=local_page)
    back_button.place(x= 300, y = 530)

    
    #back_button.place(x= 250, y = 500)
    #back_button.grid(column=1, row=0, padx=5, sticky=tk.EW)
    # cells = Grid(size, c, players, colors, player_number)

    # ttk.Separator(orient='horizontal').pack()

    # players = []
    # for i in range(0, player_number):
    #     players.append(Player(i, colors[i]))

    # c = tk.Canvas(root, height=root.winfo_height(),
    #               width=root.winfo_width(), bg='white')
    # c.pack()
    # cells = Grid(grid_size, c, players, player_number)
    # c.bind('<Configure>', cells.grid)
    # c.bind('<Button-1>', cells.numbering)

    # def client():
    #     n=Network()


    # start_new_thread(client,())
    root.mainloop()