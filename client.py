import socket
import tkinter as tk
from tkinter import ttk
from chainRxa2 import call_join_start

selected_playersize = 2
selected_gridSize = 8
values = [i for i in range(2, 11)]


def call_join(
    root, local_page, widget_destroy, image_frame, button_style, home_page, isHost
):

    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    def start(ip):
        # print(selected_playersize, selected_gridSize)
        if len(ip) == 0:
            ip = ipaddress
        # print("from start=",ip)
        call_join_start(
            root,
            local_page,
            call_join,
            widget_destroy,
            home_page,
            image_frame,
            selected_playersize,
            selected_gridSize,
            button_style,
            isHost,
            ip,
        )

    widget_destroy(root)
    image_frame()

    new_frame = ttk.Frame(root, relief="raised", borderwidth=2)
    new_frame.place(x=210, y=512.5)
    text = "IP Address: "

    def total_player(event):
        global selected_playersize
        selected_playersize = player_size.get()

    def total_grid(event):
        global selected_gridSize
        selected_gridSize = grid_size.get()

    ipaddr = tk.StringVar()
    if not isHost:

        ip_label = ttk.Label(new_frame, style="W.TLabel", text=text)
        ip_label.grid(column=0, row=0, padx=5, sticky=tk.N)

        # ipaddr = tk.StringVar()
        # ipaddress.set("192.168.000.000")
        ip_entry = ttk.Entry(new_frame, textvariable=ipaddr, style="W.TEntry", width=30)
        ip_entry.grid(column=1, row=0, sticky=tk.W)

        def focus_in(*args):
            ip_entry.delete(0, "end")

        ip_entry.bind("<FocusIn>", focus_in)
        ip_entry.insert(0, "Enter IP address")
        # ipaddress = ipaddr.get()

    else:
        text = f"Your IP Address is: {ipaddress}"

        ip_label = ttk.Label(new_frame, style="W.TLabel", text=text)
        ip_label.grid(column=0, row=0, padx=5, sticky=tk.N)

        player_size = ttk.Combobox(new_frame)
        player_size["values"] = values[:7]
        player_size["state"] = "readonly"
        player_size["style"] = "W.TCombobox"
        player_size.current(0)
        player_size.grid(column=1, row=1, sticky=tk.W)
        player_size.bind("<<ComboboxSelected>>", total_player)

        text = ttk.Label(new_frame, text="No of Players: ", style="W.TLabel")
        text.grid(column=0, row=1, sticky=tk.W)

        grid_size = ttk.Combobox(new_frame)
        grid_size["values"] = values[6:]
        grid_size["state"] = "readonly"
        grid_size["style"] = "W.TCombobox"
        grid_size.current(0)
        grid_size.grid(column=1, row=2, sticky=tk.W)
        grid_size.bind("<<ComboboxSelected>>", total_grid)

        text = ttk.Label(new_frame, text="Grid Size: ", style="W.TLabel")
        text.grid(column=0, row=2, sticky=tk.W)

        for widget in new_frame.winfo_children():
            widget.grid(padx=5, pady=3)

    submit_button = ttk.Button(
        new_frame, text="Submit", style="W.TButton", command=lambda: start(ipaddr.get())
    )
    submit_button.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)

    back_button = ttk.Button(
        new_frame, text="Back", style="W.TButton", command=local_page
    )
    back_button.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)
    root.mainloop()
