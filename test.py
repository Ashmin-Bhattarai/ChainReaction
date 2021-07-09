from server import *
choice=input("1 for host, 2 for join")
if choice =="1":
    server()
    client()
else:
    client()
