#to create a windows
# from tkinter import*
# root=Tk ()
# root.mainloop()

#to add title
# from tkinter import*
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('130x200')
# root.mainloop()


#placing lable
# from tkinter import *
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('130x200')
# l1=Label(root,text="we are python lobbi-ian")
# l1.pack()
# root.mainloop()



#to create a button
# from tkinter import *
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('700x200')
# l1=Label(root,text="To register")
# l1.pack()
# def clicked():
#     print("I am clicked")
# btn=Button(root,text="click",command=clicked)
# btn.pack()
# #root.geometry("700x200")
# root.mainloop()

#to enter anything

#to add title
# from tkinter import*
# root=Tk ()
# root.title(" welcome to python lobby")
# root.geometry('130x200')
# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# label = Label(root, text="This is Image").pack(side=TOP, pady=10)

# path = PhotoImage(file="C:/Users/HP/Pictures/flower.png")
# label_image = Label(root, image=path,width=400, height=400)
# label_image.pack()

# root.geometry("600x440")
# root.title("PythonLobby.com")
# root.mainloop()



#lixtbox widget
# from tkinter import*
# from tkinter import ttk
# root =Tk()

# Listbox=Listbox(root,width=45,height=15)
# Listbox.pack(pady=70)

# Listbox.insert(0,"c")
# Listbox.insert(1,"c++")
# Listbox.insert(2,"java")
# Listbox.insert(3,"python")


# root.geometry("400x240")
# root.title("adich keri vaa.com")
# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# root= Tk()



# pw=ttk.PanedWindow(root, orient=HORIZONTAL) 
# pw.pack(fill=BOTH, expand=True)


# frame1= Frame (pw, relief=SUNKEN, bg='lightblue') 
# frame2 =Frame(pw, relief=SUNKEN, bg='lightgreen')


# pw.add(frame1, weight=1)
# pw.add(frame2, weight=3)



# root.geometry("400x240")

# root.title("PythonLobby.com")

# root.mainloop()

from tkinter import*
root = Tk()
variable =StringVar(root)
variable.set("COLOURS")


option_menu = OptionMenu(root, variable, "yellow",
                         "Blue","Green","Purplet","Black","White")
option_menu.pack()
root.geometry("400x240")
root.mainloop()


