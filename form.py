from email.encoders import encode_base64
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
 
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['fname'])
    e3.insert(0,select['lname'])
    e4.insert(0,select['address'])
    e5.insert(0,select['program'])
    e6.insert(0,select['status'])
    e7.insert(0,select['country'])
   
 
 
def Add():
    studid = e1.get()
    studfname = e2.get()
    studlname = e3.get()
    studaddress = e4.get()
    studprogram = e5.get()
    studstatus = e6.get()
    studcountry = e7.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payroll")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  registation (id,fname,lname,address,program,status,country) VALUES (%s, %s, %s, %s, %s, %s, %s)"
       val = (studid,studfname,studlname,studaddress,studprogram,studstatus,studcountry)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Student inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
    studid = e1.get()
    studfname = e2.get()
    studlname = e3.get()
    studaddress = e4.get()
    studprogram = e5.get()
    studstatus = e6.get()
    studcountry = e7.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payroll")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  registation set fname= %s,lname= %s,address= %s,program= %s,status= %s,country= %s  where id= %s"
       val = (studfname,studlname,studaddress,studprogram,studstatus,studcountry,studid)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    studid = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payroll")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from registation where id = %s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="payroll")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,fname,lname,address,program,status,country FROM registation")
        records = mycursor.fetchall()
        print(records)
 
        for i, (id,fname,lname,address,program,status,country) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id,fname,lname,address,program,status,country))
            mysqldb.close()
 
root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
global e5
global e6
global e7
# by hrs
tk.Label(root, text="Student Registation Form", fg="orange", font=(None, 20)).place(x=550, y=5)
 
tk.Label(root, text="ID").place(x=400, y=70)
Label(root, text="FName").place(x=400, y=100)
Label(root, text="LName").place(x=400, y=130)
Label(root, text="Addres").place(x=400, y=160)
Label(root, text="Program").place(x=700, y=70)
Label(root, text="Status").place(x=700, y=100)
Label(root, text="Country").place(x=700, y=130)
 
e1 = Entry(root)
e1.place(x=500, y=70)
 
e2 = Entry(root)
e2.place(x=500, y=100)
 
e3 = Entry(root)
e3.place(x=500, y=130)
 
e4 = Entry(root)
e4.place(x=500, y=160)

e5 = Entry(root)
e5.place(x=900, y=70)

e6 = Entry(root)
e6.place(x=900, y=100)

e7 = Entry(root)
e7.place(x=900, y=130)
 
Button(root, text="Add",command = Add,height=2, width= 20).place(x=450, y=230)
Button(root, text="update",command = update,height=2, width= 20).place(x=650, y=230)
Button(root, text="Delete",command = delete,height=2, width= 20).place(x=850, y=230)
 
cols = ('id','fname','lname','address','program','status','country')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=60, y=300)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()