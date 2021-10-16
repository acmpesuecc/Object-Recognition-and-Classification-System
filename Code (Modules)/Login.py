from tkinter import *
from functools import partial
import tkinter.messagebox

#def validateLogin(username,password) :
#	print("Username entered : ", username.get())
#	print("password entered : ", password.get())
#	return

#window
tkWindow = tkinter.Tk()  
tkWindow.geometry('300x250')  
tkWindow.title('Login Page')

#username label and text entry box
usernameLabel = Label(tkWindow,text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

# Function to respond to Click on Login
def onClick():
	tkinter.messagebox.showinfo("Confirming Login","Login Succesful!")

#dictionary to store user,pwd for user profiles
data={}

# Storing data in a text file in dictionary form
def adduser():
	user = username.get()
	pwd = password.get()
	data[user] = pwd
	addloguser = open ("database.txt", "a")
	addloguser.write(str(data))
	addloguser.close()
	#Confirming Login Succesful
	onClick()
	#Closing all windows
	tkWindow.quit
	exit(0)
	
#login button
loginButton = Button(tkWindow, text="Login", command=adduser).grid(row=4, column=1) 
tkWindow.mainloop()
