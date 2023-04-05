from tkinter import *

##Functionality

def userEntered():
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def passEntered():
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

##def hide():
    

#GUI SECTION
        
loginWindow=Tk()
loginWindow.geometry('1200x750+50+50')
loginWindow.resizable(0,0)
loginWindow.title('Login')
backgroundImage=PhotoImage(file='Driving bg.png')

backgroundLabel=Label(loginWindow,image=backgroundImage)
backgroundLabel.place(x=0,y=0)


heading=Label(loginWindow,text='USER LOGIN',font=('Calibri',25,'bold'))
heading.place(x=850,y=50)

#USERNAME ENTRY
usernameEntry=Entry(loginWindow,width=25,font=('Calibri',14,'bold'))
usernameEntry.place(x=850,y=150)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',userEntered())


Frame(loginWindow,width=250,height=2).place(x=850,y=180)

#HEADING

heading=Label(loginWindow,text='USER LOGIN',font=('Calibri',25,'bold'))
heading.place(x=850,y=50)

#PASSWORD ENTRY
passwordEntry=Entry(loginWindow,width=25,font=('Calibri',14,'bold'))
passwordEntry.place(x=850,y=250)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',passEntered())

frame2=Frame(loginWindow,width=250,height=2)
frame2.place(x=850,y=280)

##Login Button
loginButton=Button(loginWindow,text='Login',font=('Open Sans',18,'bold'),fg='blue',bg='blue',activeforeground='white',activebackground='blue',cursor='hand2',bd=0,width=19)

#Making a button
eyeButton=Button(loginWindow,command=hide)
eyeButton.place(x=1075,y=278)
 
loginWindow.mainloop()
