#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main  
# root window 
master.geometry("600x300") 
  
    
  
# function to open a new window  
# on a button click 
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("login ") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text =" New login page").pack() 
  
  
label = Label(master,  
              text ="Capstone supervisor alloction portal for LPU") 
  
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="login",  
             command = openNewWindow) 
btn.pack(pady = 10) 
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("This is a new user page") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is a new us page").pack() 
  

 #label = Label(master,  text ="Capstone supervisor alloction portal for LPU") 
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="New user",  
             command = openNewWindow) 
btn.pack(pady = 10) 
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("supervisor") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is the page of supervisor").pack() 
  
  
#label = Label(master,   text ="Capstone supervisor alloction portal for LPU") 
  
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="New Supervisor",  
             command = openNewWindow) 
btn.pack(pady = 10) 
      
# mainloop, runs infinitely 
mainloop() 


# In[ ]:



#this is the the program of login page

import tkinter as tk 
import mysql.connector  
from tkinter import * 
import PIL 
   
  
def submitact(): 
      
    user = Username.get() 
    passw = password.get() 
   
    print(f"The name entered by you is {user} {passw}") 
   
    #logintodb(user, passw) 
   
   
def logintodb(user, passw): 
      
    # If paswword is enetered by the  
    # user 
    if passw: 
        db = mysql.connector.connect(host ="localhost", 
                                     user = user, 
                                     password = passw, 
                                     db ="College") 
        cursor = db.cursor() 
          
    # If no password is enetered by the 
    # user 
    else: 
        db = mysql.connector.connect(host ="localhost", 
                                     user = user, 
                                     db ="College") 
        cursor = db.cursor() 
          
    # A Table in the database 
    savequery = "select * from STUDENT"
      
    try: 
        cursor.execute(savequery) 
        myresult = cursor.fetchall() 
          
        # Printing the result of the 
        # query 
        for x in myresult: 
            print(x) 
        print("Query Excecuted successfully") 
          
    except: 
        db.rollback() 
        print("Error occured") 
   
   
root = tk.Tk() 
root.geometry("300x300") 
root.title("DBMS Login Page") 
   
C = Canvas(root, bg ="blue", height = 250, width = 300) 
  
# Definging the first row 
lblfrstrow = tk.Label(root, text ="Username -", ) 
lblfrstrow.place(x = 50, y = 20) 
  
Username = tk.Entry(root, width = 35) 
Username.place(x = 150, y = 20, width = 100) 
   
lblsecrow = tk.Label(root, text ="Password -") 
lblsecrow.place(x = 50, y = 50) 
  
password = tk.Entry(root, width = 35) 
password.place(x = 150, y = 50, width = 100) 
  
submitbtn = tk.Button(root, text ="Login",  
                      bg ='blue', command = submitact) 
submitbtn.place(x = 150, y = 135, width = 55)

  
root.mainloop() 


# In[ ]:




