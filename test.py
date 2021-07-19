import tkinter as ttk
def display(ipaddress):
    print("ipadress=",ipaddress)

root=ttk.Tk()
text = "IP Address: "
# new_frame = ttk.Frame(root, relief='raised', borderwidth=2)
# new_frame.place(x=210, y=512.5)
ip_label = ttk.Label(root,text=text)
ip_label.grid(column=0, row=0, padx=5)
ipaddr = ttk.StringVar()
ip_entry = ttk.Entry(root, textvariable=ipaddr, width=30)
ip_entry.grid(column=1, row=0)
# ipaddress = ipaddr.get()

submit_button = ttk.Button(root, text="Submit", command=lambda:display(ipaddr.get()))
submit_button.grid(column=0, row=3, padx=5, pady=5)
root.mainloop()
