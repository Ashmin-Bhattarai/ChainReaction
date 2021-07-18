from offline_screen import *
from client import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
#change

root = tk.Tk()
root.title('Chain Reaction')
root.geometry("800x800")
root.resizable(0, 0)
font = {'font': ('Arial', 10, 'bold'), 'background': '#EE018B'}

img = ImageTk.PhotoImage(Image.open("mainMenu.jpg"))

button_style = ttk.Style()
button_style.theme_use('clam')
button_style.configure('W.TButton', **font)
button_style.configure('W.TCheckbutton', **font)
button_style.configure('W.TLabel', **font)
button_style.configure('W.TLabel', **font)
button_style.configure('W.TEntry', **font)
button_style.map('W.TButton', background=[('active', '#00FABC')])

def image_frame():
    main_image_frame = ttk.Label(root, image=img)
    main_image_frame.place(x=0, y=0, relwidth=1, relheight=1)
    main_image_frame.image = img


def home_page():
    widget_destroy(root)
    image_frame()
    button_frame = ttk.Frame(root, relief='raised', borderwidth=2)
    button_frame.place(x=365, y=500)
    offline_button = ttk.Button(
        button_frame, text="Offline", style='W.TButton', command=offline_page)
    offline_button.grid(column=0, row=1, sticky=tk.W)
    # command = lambda: fun(parameter)
    local_button = ttk.Button(
        button_frame, text="Local", style='W.TButton', command=local_page)
    local_button.grid(column=0, row=2, sticky=tk.W)
    settings_button = ttk.Button(
        button_frame, text="Settings", style='W.TButton', command=settings_page)  # lambda: [play_sound('soundeffects/explode.wav'), settings_page()]
    settings_button.grid(column=0, row=3, sticky=tk.W)

    root.mainloop()


def local_page():
    widget_destroy(root)
    image_frame()
    button_frame = ttk.Frame(root)
    button_frame.place(x=360, y=500)
    
    host_button = ttk.Button(button_frame, text="Host",
                             style='W.TButton', command=home_page)
    host_button.grid(column=0, row=0, sticky=tk.W)
    
    join_button = ttk.Button(button_frame, text="Join",
                             style='W.TButton', command=join_page)
    join_button.grid(column=0, row=1, sticky=tk.W)

    root.mainloop()


def settings_page():
    widget_destroy(root)
    image_frame()
    play_sound = tk.StringVar()
    sound_button = ttk.Checkbutton(root, text='Sound', style='W.TCheckbutton', command=lambda: print(
        play_sound), variable=play_sound, onvalue="True", offvalue="False")
    sound_button.place(x=360, y=450)
    back_button = ttk.Button(
        root, text="Back", style='W.TButton', command=home_page)
    back_button.place(x=360, y=500)
    root.mainloop()


def offline_page():
    widget_destroy(root)
    mainScreen(root, home_page, image_frame, button_style)

def join_page():
    widget_destroy(root)
    call_join(root, local_page, widget_destroy, image_frame, "8", button_style)

if __name__ == "__main__":
    home_page()
