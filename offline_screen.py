from chainRxa2 import call_this
import tkinter as tk
from tkinter import ttk

values = [i for i in range(2, 11)]
selectedPlayer = 2
selectedGridSize = 8


def widget_destroy(root):
    for widgets in root.winfo_children():
        widgets.destroy()


def join_start(root, home_page, image_frame, button_style):
    call_join(root, mainScreen, widget_destroy, home_page, image_frame,
              selectedPlayer, selectedGridSize, button_style)

def mainScreen(root, home_page, image_frame, button_style):

    def playerSelected(event):
        global selectedPlayer
        selectedPlayer = no_of_players.get()

    def gridSize(event):
        global selectedGridSize
        selectedGridSize = grid_size.get()

    def gameStart():
        global selectedPlayer
        widget_destroy(root)
        call_this(root, mainScreen, widget_destroy, home_page, image_frame,
                  selectedPlayer, selectedGridSize, button_style)

    image_frame()
    player_seclection_frame = ttk.Frame(
        root, relief='raised', borderwidth=2)
    player_seclection_frame.place(x=271, y=512.5)

    no_of_players = ttk.Combobox(player_seclection_frame)
    no_of_players['values'] = values[:7]
    no_of_players['state'] = 'readonly'
    no_of_players['style'] = 'W.TCombobox'
    no_of_players.current(0)
    no_of_players.grid(column=1, row=0, sticky=tk.W)
    no_of_players.bind('<<ComboboxSelected>>', playerSelected)

    text = ttk.Label(player_seclection_frame,
                     text="No of Players: ", style='W.TLabel')
    text.grid(column=0, row=0, sticky=tk.W)

    grid_size = ttk.Combobox(player_seclection_frame)
    grid_size['values'] = values[6:]
    grid_size['state'] = 'readonly'
    grid_size['style'] = 'W.TCombobox'
    grid_size.current(0)
    grid_size.grid(column=1, row=1, sticky=tk.W)
    grid_size.bind('<<ComboboxSelected>>', gridSize)

    text = ttk.Label(player_seclection_frame,
                     text="Grid Size: ", style='W.TLabel')
    text.grid(column=0, row=1, sticky=tk.W)

    for widget in player_seclection_frame.winfo_children():
        widget.grid(padx=5, pady=3)

    start_button_frame = ttk.Frame(root, relief="raised", borderwidth=2)
    start_button_frame.place(x=300, y=606)
    start_btn = ttk.Button(start_button_frame, text="start",
                           style='W.TButton', command=gameStart)
    back_btn = ttk.Button(start_button_frame, text="Back",
                          style='W.TButton', command=lambda: home_page())
    start_btn.grid(column=0, row=0, sticky=tk.W)
    back_btn.grid(column=1, row=0, padx=3, sticky=tk.W)
    root.mainloop()


if __name__ == "__main__":
    mainScreen()
