from tkinter import*
from tkinter import ttk
root=Tk ()
root.geometry('360x560')
root.title(" ")


heading_font_style=('Myriad pro',24,"bold")
heading_font_color="black"
heading_lable=Label( root,text="Instagram",font=heading_font_style,fg=heading_font_color)
heading_lable.pack(side=TOP, pady=80)

font_style2=("arial",12)
email_font=("arial",12)
forgot_password_font=("arial",9)
forgot_password_font_color="blue"

lable_login=Label(root,text="Enter email",font=font_style2)
lable_login.pack(pady=4)
email_entry=Entry(root,font=email_font)
email_entry.pack()

lable_password=Label(root,text="Enter password",font=font_style2)
lable_password.pack(pady=4)
password_entry=Entry(root,font=email_font)
password_entry.pack()


lable_forgot_password=Label(root,text="Forgot password ?",font=forgot_password_font,fg=forgot_password_font_color)
lable_forgot_password.pack(pady=4)


login_btn=Button(root,text="login")
login_btn.pack(pady=40)
root.mainloop()



