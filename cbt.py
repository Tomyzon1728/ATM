# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:17:13 2019

@author: Ajayi Raymond T
"""

from tkinter import *
from PIL import Image,ImageTk
import os
answer = ''
score = ''
def RegisterUser ():
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info,'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()
    
    username_entry.delete(0,'end')
    password_entry.delete(0,'end')
    
    Label(screen1,text = 'Registration Sucess',fg = 'green',font = ('calibri',11)).pack()
    
def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('300x250')
    #screen1.wm_iconbitmap('aduser.ico')
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1,text = 'Please Enter Details Below').pack()
    Label(screen1,text = '',fg = 'green',font = ('calibri',11)).pack()
    Label(screen1,text = 'Username  * ' ,fg = 'green',font = ('calibri',11)).pack()
    
   
    
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1,text = 'Password  * ' ,fg = 'green',font = ('calibri',11)).pack()
    password_entry = Entry(screen1, textvariable = password, show = '*')
    password_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1,text = 'Register',height = '2', width = '30', bg='#FFFACD', command = RegisterUser).pack()
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
    #screen3.wm_iconbitmap('aduser.ico')
    Label(screen3,text = 'Sucess').pack()
    Button(screen3,text = 'LOGIN SUCESS',command = test,bg = 'green').pack()
def test():
    screen6 = Toplevel(screen)
    screen6.title('CBT Test')
    #screen6.wm_iconbitmap('computer.ico')



    #img = Image.open('shugar.JPG')
    #img1 = ImageTk.PhotoImage(img, master = root)
    frm1 = Label(screen6,anchor='nw',relief = SUNKEN,compound ='left',bg = 'navy blue',fg= '#00ffff', height = 5,text = ' SHUGARREYLUMINATIONS \nComputer Based Test', font =('courier',20, 'bold'))
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
    qfrm = Label(frm ,text = '1. What is the name of the first democratic president?',height =1)
    qfrm.pack(side = 'left')
#----------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group,text = 'Olusegun Obasanjo', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group,text = 'Muhammadu  Buhari  ', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group,text = 'Goodluck Jonathan', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group,text = 'Sukar  Dimka  ', value = 'd').pack(side = 'left')

#------------------------------------n0 2----------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '2. What year did Nigeria become a republic?',height = 2)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group1,text = '1960', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group1,text = '  1958  ', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group1,text = '1963', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group1,text = '  1914  ', value = 'd').pack(side = 'left')

#--------------------------------------n0 3------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '3. What is the name of the first Head of state?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group2,text = 'Murtala Mohammed', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group2,text = 'Aguyi Ironsi ', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group2,text = 'Yakubu Gowon', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group2,text = 'Ibrahim Banbagida', value = 'd').pack(side = 'left')

#-------------------------------------------------n0 4---------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '4. The current Nigerian constitution was last ammended?',height = 2)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group3,text = '1945', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group3,text = '1979 ', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group3,text = '1999', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group3,text = '1983', value = 'd').pack(side = 'left')

#-----------------------------------------n0 5--------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '5. Who was the first Nigerian President?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group4,text = 'Tafawa Balewa', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group4,text = 'Nnamdi Azikiwe', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group4,text = 'Shehu Shagari', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group4,text = 'Olusegun Obasanjo', value = 'd').pack(side = 'left')

#--------------------------------------------n0 6---------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '6. When was the first Nigerian military coup?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group5,text = '1958', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group5,text = '1975', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group5,text = '1985', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group5,text = '1966', value = 'd').pack(side = 'left')

#-----------------------------------------n0 7---------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '7. Who was the first Nigerian interim President?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group6,text = 'Ernest Sonekan', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group6,text = 'Abubakar Abdusalam', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group6,text = 'Moshood Abiola', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group6,text = 'Jaja Wackuwku', value = 'd').pack(side = 'left')

#-----------------------------------------------n0 8-------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '8. What year did Nigeria win her first international gold- medal?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group7,text = '1954', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group7,text = '1950', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group7,text = '1996', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group7,text = '2012', value = 'd').pack(side = 'left')

#------------------------------------------no 9-------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '9. Who master-minded the first Nigerian military coup?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group8,text = 'Kaduna Nzeogwu', value = 'a').pack(side = 'left')

    Radiobutton(frm,variable = group8,text = 'Emmanuel Ifeajuna', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group8,text = 'Gideon Okar', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group8,text = 'Mamman Vatsa', value = 'd').pack(side = 'left')

#----------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    qfrm = Label(frm ,text = '10.Nigeria is currently in her?',height = 1)
    qfrm.pack(side = 'left')

#-------------------------------------------------------------------------------------------
    frm = Label(screen6,height = 1)
    frm.pack(side = 'top',fill = BOTH)
    frm.grid_propagate(0)

    Radiobutton(frm,variable = group9,text = 'Fourth Republic', value = 'a').pack(side = 'left')


    Radiobutton(frm,variable = group9,text = 'Fisrt Republic', value = 'b').pack(side = 'left')

    Radiobutton(frm,variable = group9,text = 'Fifth Republic', value = 'c').pack(side = 'left')

    Radiobutton(frm,variable = group9,text = 'Second Republic', value = 'd').pack(side = 'left')


    frm2 = Label(screen6, bg = 'navy blue', height = 3)
    frm2.pack(side = 'bottom',fill = BOTH)
    btn = Button(frm2,relief = GROOVE,text = 'S U B M I T',padx= 16, bd = 2, fg='navy blue',font =('serif',10, 'bold'),bg = '#00ffff',command =Score)
    btn.pack(side = 'left')
def PasswordNotVerified():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title('Unsucessful Login')
    screen4.geometry('300x250')
    #screen4.wm_iconbitmap('aduser.ico')
    Label(screen4,text = 'Unverified Password').pack()
    Button(screen4,text = 'LOGIN FAILED',command = delete3,bg = 'red').pack() 
def UserNotFound():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title('Unsucessful Login')
    screen5.geometry('300x250')
    #screen5.wm_iconbitmap('aduser.ico')
    Label(screen5,text = 'User Not Found').pack()
    Button(screen5,text = 'LOGIN FAILED',command = delete4,bg = 'red').pack()
    

def LoginVerify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,'end')
    password_entry1.delete(0,'end')
    
    file_list = os.listdir()
    if username1 in  file_list:
        file1 = open(username1, 'r')
        verify = file1.read().splitlines()
        if password1 in verify:
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
    #screen2.wm_iconbitmap('aduser.ico')
    Label(screen2,text = 'Please Enter Details Below to Login').pack()
    Label(screen2, text = 'Password').pack()
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1

    Label(screen2,text = 'Username  * ').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = 'Password *').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = '*')
    password_entry1.pack()
    Label(screen2, text = '').pack()
    Button(screen2,text = 'Login',height = '1', fg='#F08080', bg='#FFFACD', width = '30', command = LoginVerify).pack()

def MainScreen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('SignUp')
    #screen.wm_iconbitmap('aduser.ico')
    Label(text = 'Management Register Login System',bg = 'orange',width= '300',height= '2',font = ('calibri',13)).pack()
    Button(text = 'Login',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command = Login).pack()
    Label( text = '').pack()
    Button(text = 'Register',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command = Register).pack()
     
    screen.mainloop()

MainScreen()