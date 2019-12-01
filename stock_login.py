from tkinter import *
from tkinter import messagebox
from PIL import ImageTk     #Pillow
from ims_stock import Stock
import pymysql

class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #===========All images=============#
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.png")
        self.user_icon=ImageTk.PhotoImage(file="images/man-user.png")
        self.pass_icon=ImageTk.PhotoImage(file="images/password.png")
        self.logo_icon=ImageTk.PhotoImage(file="images/logo.png")

        #===========Variables=============#
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=450,y=250)

        logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text=" Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20)
        txtuser=Entry(Login_Frame,textvariable=self.uname,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text=" Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20)
        txtpass=Entry(Login_Frame,show="*",textvariable=self.pass_,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,command=self.login,text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required")
            return
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        statement=f"select * from users where username='{self.uname.get()}' and pass='{self.pass_.get()}'"
        cur.execute(statement)
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showerror("Error","Invalid username or password")
            return
        messagebox.showinfo("Successful","Welcome ")
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Stock(self.root)
        con.commit()
        con.close()

root=Tk()
obb=login_system(root)
root.mainloop()
