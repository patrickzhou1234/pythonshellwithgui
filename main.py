import os
import os.path
import socket
import tkinter

print("\x1b[37m", "pzrepl's™ shell started!")
while True:
  inp = input(">")
  for i in range(10):
    if str(i) in inp:
      print("\x1b[31m", "Numbers are invalid", "\x1b[37m")
      break

  if "list" in inp:
    if os.path.exists("./"+inp[5:]+"/"):
      print(os.listdir("./"+inp[5:]+"/"))
    else:
      print("\x1b[31m", "This directory does not exist.", "\x1b[37m")

  if "delete " in inp:
    if os.path.exists("./"+inp[7:]):
      os.remove("./"+inp[7:])
      print("\x1b[32m", "Successfully deleted file.", "\x1b[37m")
    else:
      print("\x1b[31m", "This file does not exist.", "\x1b[37m")

  if inp == "clear":
    clear = lambda: os.system("clear")
    clear()

  if "deletefolder " in inp:
    if os.path.exists("./"+inp[13:]):
      os.rmdir("./"+inp[13:])
      print("\x1b[32m", "Successfully deleted folder.", "\x1b[37m")
    else:
      print("\x1b[31m", "This folder does not exist.", "\x1b[37m")

  if inp == "getip":
    print(socket.gethostbyname(socket.gethostname()))

  if "make " in inp:
    if os.path.exists("./"+inp[5:]):
      print("\x1b[31m", "This file already exists.", "\x1b[37m")
    else:
      os.mknod("./"+inp[5:])
      print("\x1b[32m", "Successfully created file.", "\x1b[37m")

  if "makefolder " in inp:
    if os.path.exists("./"+inp[11:]):
      print("\x1b[31m", "This folder already exists.", "\x1b[37m")
    else:
      os.mkdir("./"+inp[11:])
      print("\x1b[32m", "Successfully created folder.", "\x1b[37m")

  if inp == "gui":
    print("\x1b[32m", "Showing Gui.", "\x1b[37m")
    textbox = tkinter.Text()
    textbox.config(width=30, height=1)
    textbox.pack()

    def showcont():
      if os.path.exists("./"+textbox.get("1.0", 'end-1c')):
        file = open("./"+textbox.get("1.0", 'end-1c'), "r")
        print(file.read())
        file.close()
      else:
        print("\x1b[31m", "\nThis file does not exist. ", "\x1b[37m")

    button = tkinter.Button(text="Open", command=showcont)
    button.pack(pady=100, padx=100)
    lab = tkinter.Label(text="Choose a File")
    lab.pack()

  if inp == "help":
    print("Commands: \nlist\ndelete\nclear\ndeletefolder\nmake\nmakefolder\ngui")

  if inp == "help list":
    print("syntax: list <path>\naction: listing all directories and files in path. ")

  if inp == "help delete":
    print("syntax: delete <filepath>\naction: deleting a specified file. ")

  if inp == "help deletefolder":
    print("syntax: deletefolder <directorypath>\naction: deleting a specified directory. ")

  if inp == "help clear":
    print("syntax: 'clear'\naction: clears terminal. ")
  
  if inp == "help make":
    print("syntax: make <filepath>\naction: creates desired file. ")

  if inp == "help makefolder":
    print("syntax: makefolder <directorypath>\naction: creates desired folder. ")

  if inp == "help gui":
    print("syntax: 'gui'\naction: creates gui interface. ")
