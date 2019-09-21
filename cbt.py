# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:17:13 2019

@author: Ajayi Raymond T
"""

from tkinter import *
from PIL import Image,ImageTk
import os
import mysql.connector
answer = ''
score = ''
Score = ''
mycon = mysql.connector.connect(host='localhost',user= 'root',password='',database='cbt_db')
mycursor= mycon.cursor(dictionary = True)
def test():
    screen6 = Toplevel(screen)
    screen6.title('CBT Test')
    screen6.wm_iconbitmap('computer.ico')



    img = Image.open('shugar.JPG')
    img1 = ImageTk.PhotoImage(img, master = screen6)
    frm1 = Label(screen6,anchor='nw',image= img1,relief = SUNKEN,compound ='left',bg = 'navy blue',fg= '#00ffff', height = 73,text = ' SHUGARREYLUMINATIONS \nComputer Based Test', font =('courier',20, 'bold'))
    frm1.pack(side = 'top',fill = BOTH)


    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)



    group = StringVar()
    group1 = StringVar()
    group2= StringVar()
    group3 = StringVar()
    group4 = StringVar()
    group5 = StringVar()
    group6 = StringVar()
    group7 = StringVar()
    group8 = StringVar()
    group9 = StringVar()
    val = group.get()
    val1 = group1.get()
    val2 = group2.get()
    val3 = group3.get()
    val4 = group4.get()
    val5 = group5.get()
    val6 = group6.get()
    val7 = group7.get()
    val8 = group8.get()
    val9 = group9.get()

#-----------------------------------n0 1-------------------------------------------------------
    qfrm = Label(frm ,text = '1. What is the name of the first democratic president?',height =1, font =('courier',11, 'bold'))
    qfrm.pack(side = 'left')
#----------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group,text = 'Olusegun Obasanjo', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group,text = 'Muhammadu  Buhari  ', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group,text = 'Goodluck Jonathan', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group,text = 'Sukar  Dimka  ', value = 'd',tristatevalue=0).pack(side = 'left')

#------------------------------------n0 2----------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '2. What year did Nigeria become a republic?',height = 2, font =('courier',11, 'bold'))
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group1,text = '1960', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group1,text = '  1958  ', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group1,text = '1963', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group1,text = '  1914  ', value = 'd',tristatevalue=0).pack(side = 'left')

#--------------------------------------n0 3------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm , font =('courier',11, 'bold'),text = '3. What is the name of the first Head of state?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group2,text = 'Murtala Mohammed', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group2,text = 'Aguyi Ironsi ', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group2,text = 'Yakubu Gowon', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group2,text = 'Ibrahim Banbagida', value = 'd',tristatevalue=0).pack(side = 'left')

#-------------------------------------------------n0 4---------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm , font =('courier',11, 'bold'),text = '4. The current Nigerian constitution was last ammended?',height = 2)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group3,text = '1945', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group3,text = '1979 ', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group3,text = '1999', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group3,text = '1983', value = 'd',tristatevalue=0).pack(side = 'left')

#-----------------------------------------n0 5--------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm , font =('courier',11, 'bold'),text = '5. Who was the first Nigerian President?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group4,text = 'Tafawa Balewa', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group4,text = 'Nnamdi Azikiwe', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group4,text = 'Shehu Shagari', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group4,text = 'Olusegun Obasanjo', value = 'd',tristatevalue=0).pack(side = 'left')

#--------------------------------------------n0 6---------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm , font =('courier',11, 'bold'),text = '6. When was the first Nigerian military coup?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group5,text = '1958', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group5,text = '1975', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group5,text = '1985', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group5,text = '1966', value = 'd',tristatevalue=0).pack(side = 'left')

#-----------------------------------------n0 7---------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm, font =('courier',11, 'bold') ,text = '7. Who was the first Nigerian interim President?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group6,text = 'Ernest Sonekan', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group6,text = 'Abubakar Abdusalam', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group6,text = 'Moshood Abiola', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group6,text = 'Jaja Wackuwku', value = 'd',tristatevalue=0).pack(side = 'left')

#-----------------------------------------------n0 8-------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm, font =('courier',11, 'bold') ,text = '8. What year did Nigeria win her first international gold- medal?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group7,text = '1954', value = 'a', tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group7,text = '1950', value = 'b', tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group7,text = '1996', value = 'c', tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group7,text = '2012', value = 'd', tristatevalue=0).pack(side = 'left')

#------------------------------------------no 9-------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm, font =('courier',11, 'bold') ,text = '9. Who master-minded the first Nigerian military coup?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group8,text = 'Kaduna Nzeogwu', value = 'a',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group8,text = 'Emmanuel Ifeajuna', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group8,text = 'Gideon Okar', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group8,text = 'Mamman Vatsa', value = 'd',tristatevalue=0).pack(side = 'left')

#----------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm , font =('courier',11, 'bold'),text = '10.Nigeria is currently in her?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group9,text = 'Fourth Republic', value = 'a',tristatevalue=0).pack(side = 'left')


    Radiobutton(frm,variable = group9,text = 'Fisrt Republic', value = 'b',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group9,text = 'Fifth Republic', value = 'c',tristatevalue=0).pack(side = 'left')

    Radiobutton(frm,variable = group9,text = 'Second Republic', value = 'd',tristatevalue=0).pack(side = 'left')


    frm2 = Label(screen6, bg = 'navy blue', height = 3)
    frm2.pack(side = 'bottom',fill = BOTH)
    btn = Button(frm2,relief = GROOVE,text = 'S U B M I T',padx= 16, bd = 2, fg='navy blue',font =('serif',10, 'bold'),bg = '#00ffff',command =Score)
    btn.pack(side = 'left')
def PasswordNotVerified():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title('Unsucessful Login')
    screen4.geometry('300x250')
    screen4.wm_iconbitmap('aduser.ico')
    Label(screen4,text = 'Unverified Password', font =('courier',11, 'bold')).pack()
    Button(screen4,text = 'LOGIN FAILED',command = delete3,bg = 'red', font =('courier',10, 'bold')).pack() 
def UserNotFound():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title('Unsucessful Login')
    screen5.geometry('300x250')
    screen5.wm_iconbitmap('aduser.ico')
    Label(screen5,text = 'User Not Found', font =('courier',11, 'bold')).pack()
    Button(screen5,text = 'LOGIN FAILED',command = delete4,bg = 'red', font =('courier',10, 'bold')).pack()
    

def LoginVerify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,'end')
    password_entry1.delete(0,'end')
    
    sql = 'SELECT * FROM registration WHERE user_name = %s'
    adr = (username1,)
    mycursor.execute(sql,adr)
   
    result = mycursor.fetchall()
    
    if len(result) > 0:
    
        if password1 == result[0]['password']:
            LoginSucess()
        else:
            PasswordNotVerified()
    else:
        UserNotFound()
    
def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('Login')
    screen2.geometry('300x250')
    screen2.wm_iconbitmap('aduser.ico')
    Label(screen2,text = 'Please Enter Details Below to Login', font =('courier',9, 'bold')).pack()
    Label(screen2, text = 'Password', font =('courier',11, 'bold')).pack()
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1

    Label(screen2,text = 'Username  * ', font =('courier',11, 'bold')).pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = 'Password *', font =('courier',11, 'bold')).pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = '*')
    password_entry1.pack()
    Label(screen2, text = '').pack()
    Button(screen2,text = 'Login',height = '1', fg='navy blue', bg='#00ffff', width = '30', command = LoginVerify, font =('courier',10, 'bold')).pack()
def RegisterUser ():
    username_info = username.get()
    password_info = password.get()
    
  
    sql = 'INSERT INTO registration(user_name,password) VALUES(%s,%s)'
    val = (username_info,password_info)
    mycursor.execute(sql,val)
    mycon.commit()
    print(mycursor.rowcount,'Record Inserted successfully')
    
    username_entry.delete(0,'end')
    password_entry.delete(0,'end')
    
    Label(screen1,text = 'Registration Sucess',fg = 'green', font =('courier',11, 'bold')).pack()
    
def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('300x250')
    screen1.wm_iconbitmap('aduser.ico')
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1,text = 'Please Enter Details Below', font =('courier',11, 'bold')).pack()
    Label(screen1,text = '',fg = 'green', font =('courier',11, 'bold')).pack()
    Label(screen1,text = 'Username  * ' ,fg = 'green', font =('courier',11, 'bold')).pack()
    
   
    
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1,text = 'Password  * ' ,fg = 'green', font =('courier',11, 'bold')).pack()
    password_entry = Entry(screen1, textvariable = password, show = '*')
    password_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1,text = 'Register',height = '2', width = '30', bg='#00ffff',fg = 'navy blue', command = RegisterUser, font =('courier',10, 'bold')).pack()
def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def LoginSucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title('Sucessful Login')
    screen3.geometry('300x250')
    screen3.wm_iconbitmap('aduser.ico')
    Label(screen3,text = 'Click Button to start Test', font =('courier',11, 'bold')).pack()
    Button(screen3,text = 'Click Here',command = test,bg = 'green', font =('courier',10, 'bold')).pack()
def MainScreen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('SignUp')
    screen.wm_iconbitmap('aduser.ico')
    
    Label(text = 'Computer Based Test on\nHistory',bg = 'navy blue',fg ='#00ffff', width= '300',height= '2', font =('courier',13, 'bold')).pack()
    Label( text = '').pack()
    Button(text = 'Login', font =('courier',10, 'bold'),height = '2', fg='navy blue', bg='#00ffff', width = '30', command = Login).pack()
    Label( text = '').pack()
    Button(text = 'Register', font =('courier',10, 'bold'),height = '2', fg='navy blue', bg='#00ffff', width = '30', command = Register).pack()
    screen.mainloop()
MainScreen()