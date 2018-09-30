# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 13:01:29 2018

@author: Akshay Tyagi
"""
import pymysql
import tkinter as tk
from tkinter import messagebox 
parent= tk.Tk()

##CREATE DATABASE TABLE
def create():
    db = pymysql.connect("localhost","root","","account" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # Create table as per requirement
    sql = """CREATE TABLE EMPLOYEE(
    EMPLOYEE_ID CHAR(8) PRIMARY KEY,
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME INT )"""
    cursor.execute(sql)
    # disconnect from server
    db.close()
    messagebox.showinfo("Created", "Succesfully Created")
    return


def insert():
    global e, f, l, a, s, i
    top= tk.Toplevel()
    top.title("Insert")
    e= tk.IntVar()
    f= tk.StringVar()
    l= tk.StringVar()
    a= tk.IntVar()
    s= tk.StringVar()
    i= tk.IntVar()
    
    l2= tk.Label(top, text="Employee ID:").grid(row=0, column=0, sticky='e')
    l3= tk.Label(top, text="First Name:").grid(row=1, column=0, sticky='e')
    l4= tk.Label(top, text="Last Name:").grid(row=2, column=0, sticky='e')
    l5= tk.Label(top, text="Age:").grid(row=3, column=0, sticky='e')
    l6= tk.Label(top, text="Sex:").grid(row=4, column=0, sticky='e')
    l7= tk.Label(top, text="Income:").grid(row=5, column=0, sticky='e')
    e2= tk.Entry(top, width=20, textvariable= e).grid(row=0, column=1,padx=2, pady=2, sticky='we', columnspan=9)
    e3= tk.Entry(top, width=20, textvariable= f).grid(row=1, column=1,padx=2, pady=2, sticky='we', columnspan=9)
    e4= tk.Entry(top, width=20, textvariable= l).grid(row=2, column=1,padx=2, pady=2, sticky='we', columnspan=9)
    e5= tk.Entry(top, width=20, textvariable= a).grid(row=3, column=1,padx=2, pady=2, sticky='we', columnspan=9)
    e6= tk.Entry(top, width=20, textvariable= s).grid(row=4, column=1,padx=2, pady=2, sticky='we', columnspan=9)
    e7= tk.Entry(top, width=20, textvariable= i).grid(row=5, column=1,padx=2, pady=2, sticky='we', columnspan=9)
    b1= tk.Button(top, text="INSERT", command= insert2).grid(row=6, column= 5, padx=2, pady=2)
    
    ## Prepare SQL query to INSERT a record into the database.
    top.mainloop()
    return


def insert2():
    db = pymysql.connect("localhost","root","","account" )
    ## prepare a cursor object using cursor() method
    cursor = db.cursor()
    try:
    ## Execute the SQL command
        cursor.execute('INSERT INTO EMPLOYEE(EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s, %s)',(e.get(), f.get(), l.get(), a.get(), s.get(), i.get()))
    ## Commit your changes in the database
        db.commit()
        messagebox.showinfo("Inserted", "Succesfully Inserted")
    except:
#    ## Rollback in case there is any error
        db.rollback()
        messagebox.showerror("Error", "Could Not Insert")
    ## disconnect from server
    db.close()
    
    return



def update():
    option= messagebox.askquestion("Update", "Do you want to update this employee id?")
    if option == "yes":
         global ne
         uwindow= tk.Toplevel()
         uwindow.title("Update")
         ne= tk.IntVar()
         l8= tk.Label(uwindow, text="New Salary:").grid(row=0, column=0, sticky='e')
         e8= tk.Entry(uwindow, width=20, textvariable= ne).grid(row=0, column=1,padx=2, pady=2, sticky='we', columnspan=9)
         b2= tk.Button(uwindow, text="UPDATE", command= update2).grid(row=1, column= 5, padx=2, pady=2)
         uwindow.mainloop()
         
    else:
        messagebox.showerror("Error", "Could Not Update")
    return

def update2():
    db = pymysql.connect("localhost","root","","account" )
    ## prepare a cursor object using cursor() method
    cursor = db.cursor()
    ## Prepare SQL query to UPDATE required records
    try:
        ## Execute the SQL command
        cursor.execute('UPDATE EMPLOYEE SET INCOME = %d  WHERE EMPLOYEE_ID = %s',(ne.get(),iid.get())) 
        ## Commit your changes in the database
        db.commit()
        messagebox.showinfo("Updated", "Succesfully Updated")
        
    except:
        ## Rollback in case there is any error
        db.rollback()
        messagebox.showerror("Error", "Could Not Update")
        
    
    ## disconnect from server
    db.close()
    return


def delete():
    option= messagebox.askquestion("Delete", "Do you want to delete this employee id?")
    if option == "yes":
        db = pymysql.connect("127.0.0.1","root","","account" )
        ## prepare a cursor object using cursor() method
        cursor = db.cursor()
        ## Prepare SQL query to DELETE required records
        sql = ('DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID = %s') 
        var= (iid.get())
        try:
            ## Execute the SQL command
            cursor.execute(sql,var)
            ## Commit your changes in the database
            db.commit()
            messagebox.showinfo("Deleted", "Succesfully Deleted")
        except:
            ## Rollback in case there is any error
            db.rollback()
            messagebox.showerror("Error", "Could Not Delete")
        ## disconnect from server
        db.close()
    else:
        messagebox.showerror("Error", "Could Not Delete")
    return


def read():
    db = pymysql.connect("localhost","root","","account" )
    ## prepare a cursor object using cursor() method
    cursor = db.cursor()
    ## Prepare SQL query to INSERT a record into the database.
    sql = "SELECT * FROM EMPLOYEE WHERE EMPLOYEE_ID = '%s'" %(iid.get())
    try:
    ## Execute the SQL command
        cursor.execute(sql)
    ## Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            eid= row[0]
            fname = row[1]
            lname = row[2]
            age = row[3]
            sex = row[4]
            income = row[5]
    ## Now print fetched result
        messagebox.showinfo("Details","Employee ID=%s\nFirst Name=%s\nLast Name=%s\nAge=%d\nSex=%s\nIncome=%d" %(eid, fname, lname, age, sex, income ))
    except:
        messagebox.showerror("Error", "unable to fecth data")
    ## disconnect from server
    db.close()
    return



iid= tk.StringVar()
option= tk.IntVar()
parent.title("Account Department")

l1= tk.Label(parent, text="Employee ID:").grid(row=0, column=0, sticky='e')
e1= tk.Entry(parent, width=60, textvariable= iid).grid(row=0, column=1,padx=2, pady=2, sticky='we', columnspan=9)

r1= tk.Radiobutton(parent, text='Search', variable=option, value=1, command= read).grid(row=1, column=1, columnspan=3, sticky='w', padx=2, pady=2)
r2= tk.Radiobutton(parent, text='Update', variable=option, value=2, command= update).grid(row=1, column=4, columnspan=3, sticky='w', padx=2, pady=2)
r3= tk.Radiobutton(parent, text='Delete', variable=option, value=3, command= delete).grid(row=1, column=7, columnspan=3, sticky='w', padx=2, pady=2)

menubar= tk.Menu(parent)
menupull= tk.Menu(menubar, tearoff=0)
menupull.add_command(label= "Create Table", command= create)
menupull.add_command(label= "Insert", command= insert)
menupull.add_separator()
menupull.add_command(label= "Exit", command= parent.quit)
menubar.add_cascade(label= "Menu", menu=menupull )
parent.config(menu= menubar)

parent.mainloop()

