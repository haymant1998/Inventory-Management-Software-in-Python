from tkinter import *
from tkinter import ttk
from random import randint
import pymysql
from ims_bill import Bill_App

class Stock:
    def __init__(self,root):
        self.root=root
        self.root.title("Stock Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,bd=10,relief=GROOVE,text="Stock Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

        #===========All Variables==============

        self.item_no=StringVar()
        self.item_no.set(str(randint(1,1000)))
        self.item_name=StringVar()
        self.item_qty=IntVar()
        self.item_price=IntVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #=========Creating Menus for project=======================

        main_menu=Menu(self.root)
        self.root.config(menu=main_menu)

        fileMenu=Menu(main_menu)
        main_menu.add_cascade(label="File",menu=fileMenu)
        fileMenu.add_command(label="Bill Section", command=self.openBill)
        fileMenu.add_command(label="Exit", command=exit)

        #==========Menu ends here===================================

        #============Stock Entry Frame===============>

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame, text="Manage Stocks",bg="crimson",fg="white", font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_item_no=Label(Manage_Frame, text="Item No.",bg="crimson",fg="white", font=("times new roman",20,"bold"))
        lbl_item_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_item_no=Entry(Manage_Frame,textvariable=self.item_no,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_item_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_item_name=Label(Manage_Frame, text="Item Name",bg="crimson",fg="white", font=("times new roman",20,"bold"))
        lbl_item_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_item_name=Entry(Manage_Frame,textvariable=self.item_name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_item_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_item_price=Label(Manage_Frame, text="Item Price",bg="crimson",fg="white", font=("times new roman",20,"bold"))
        lbl_item_price.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_item_price=Entry(Manage_Frame,textvariable=self.item_price,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_item_price.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_item_qty=Label(Manage_Frame, text="Item Quantity",bg="crimson",fg="white", font=("times new roman",20,"bold"))
        lbl_item_qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_item_qty=Entry(Manage_Frame,textvariable=self.item_qty,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_item_qty.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        #===========Button Frame=============
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=8,y=400,width=430)

        Addbtn=Button(btn_Frame,command=self.add_stock,text="Add",width=9).grid(row=0,column=0,padx=8,pady=10)
        updatebtn=Button(btn_Frame,command=self.update_data,text="Update",width=9).grid(row=0,column=1,padx=8,pady=10)
        deletebtn=Button(btn_Frame,command=self.delete_data,text="Delete",width=9).grid(row=0,column=2,padx=8,pady=10)
        Clearbtn=Button(btn_Frame,command=self.clear,text="Clear",width=9).grid(row=0,column=3,padx=8,pady=10)



        #===========Detail Frame=====================

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=830,height=580)

        lbl_Search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15 ,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Item No","Item Name")
        combo_search.grid(row=0,column=1, padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,command=self.search_data,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,command=self.fetch_date,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #=============Table Frame===========

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=795,height=490)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Stock_Table=ttk.Treeview(Table_Frame, column=("item_no","item_name","qty","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Stock_Table.xview)
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("item_no",text="Item No")
        self.Stock_Table.heading("item_name",text="Item Name")
        self.Stock_Table.heading("qty",text="Quantity")
        self.Stock_Table.heading("price",text="Price")
        self.Stock_Table['show']='headings'
        self.Stock_Table.column("item_no",width=100)
        self.Stock_Table.column("item_name",width=460)
        self.Stock_Table.column("qty",width=100)
        self.Stock_Table.column("price",width=100)
        self.Stock_Table.pack(fill=BOTH,expand=1)
        self.fetch_date()
        self.Stock_Table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_stock(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        statement=f"insert into stocks values ('{self.item_no.get()}','{self.item_name.get()}',{self.item_qty.get()},{self.item_price.get()})"
        cur.execute(statement)
        con.commit()
        self.fetch_date()
        self.clear()
        con.close()

    def fetch_date(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute("select * from stocks")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.item_no.set(str(randint(1,1000)))
        self.item_name.set("")
        self.item_price.set(0)
        self.item_qty.set(0)

    def get_cursor(self,ev):
        cursor_row=self.Stock_Table.focus()
        contents=self.Stock_Table.item(cursor_row)
        row=contents['values']
        self.item_no.set(row[0])
        self.item_name.set(row[1])
        self.item_qty.set(row[2])
        self.item_price.set(row[3])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        statement=f"update stocks set item_no='{self.item_no.get()}', qty={self.item_qty.get()}, price={self.item_price.get()},name='{self.item_name.get()}' where item_no={self.item_no.get()}"
        cur.execute(statement)
        con.commit()
        self.fetch_date()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        cur.execute(f"delete from stocks where item_no='{self.item_no.get()}'")
        con.commit()
        con.close()
        self.fetch_date()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="ims")
        cur=con.cursor()
        if f'{self.search_by.get()}'=='Item No':
            statement=f"select * from stocks where item_no='{self.search_txt.get()}'"
        else:
            statement=f"select * from stocks where name='{self.search_txt.get()}'"
        cur.execute(statement)
        self.Stock_Table.delete(*self.Stock_Table.get_children())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for row in rows:
                self.Stock_Table.insert('',END, values=row)
            con.commit()
        con.close()

    def openBill(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root=Bill_App(self.root)
