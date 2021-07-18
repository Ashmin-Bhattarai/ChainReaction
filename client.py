from grid import Grid
import tkinter as tk
from tkinter import Frame, ttk
from network import *
from _thread import *

def call_join(root, local_page, widget_destroy, image_frame, grid_size, button_style):

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

    new_frame = ttk.Frame(root, relief='raised', borderwidth=2)
    new_frame.place(x=260, y=510)

    ip_label = ttk.Label(new_frame, style='W.TLabel', text="IP Address:")
    ip_label.grid(column=0, row=0, padx=5, sticky=tk.W)
    
    

    ipaddress = tk.StringVar()
    # ipaddress.set("192.168.000.000")
    ip_entry = ttk.Entry(new_frame, textvariable=ipaddress, style='W.TEntry', width=30)
    ip_entry.grid(column=1, row=0, sticky=tk.W)
    
    def focus_in(*args):
        ip_entry.delete(0, 'end')
        

    
    ip_entry.bind("<FocusIn>",focus_in)
    ip_entry.insert(0, 'Enter IP address')
    
    # print(ip_entry.focus_get())
    
    submit_button = ttk.Button(new_frame, text="Submit", style='W.TButton', command=lambda: print(f"{ipaddress.get()}"))
    submit_button.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)

    back_button = ttk.Button(new_frame, text='Back', style="W.TButton", command=local_page)
    back_button.grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)

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
