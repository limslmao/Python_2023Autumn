import pyrebase
import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry

# // Your web app's Firebase configuration
config = {
    "apiKey": "AIzaSyBTjmE7P6drIjs3D4fqthZtRKBxqKMWfU0",
    "authDomain": "fir-test-492e5.firebaseapp.com",
    "projectId": "fir-test-492e5",
    "storageBucket": "fir-test-492e5.appspot.com",
    "messagingSenderId": "596036791015",
    "appId": "1:596036791015:web:b5d06e757cb7771ccb1042",
    "databaseURL" : "" #記得手動新增
    }

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()


# create Label in login Windows
root = tk.Tk()

loginlabel = Label(root, text = 'Login Page')
accountlabel = Label(root, text = 'Account')
passwordlabel = Label(root, text = 'Password')
resultLabel = Label(root, text = "")

# 創建帳號和密碼輸入框
accountentry = Entry(root)
passwordentry = Entry(root, show="*")  # 密碼輸入會顯示為星號
signUpbutton = Button(root, text = 'Sign Up', width=10, command=lambda: addUser(root, accountentry, passwordentry))
loginbutton = Button(root, text = 'Login', width=10, command=lambda: verifyUser(root, accountentry, passwordentry))

# 放置元件
loginlabel.pack(pady=5)  # 在標籤上方添加間隔
accountlabel.pack(pady=5)
accountentry.pack(pady=5)
passwordlabel.pack(pady=5)
passwordentry.pack(pady=5)
signUpbutton.pack(pady=5)
loginbutton.pack(pady=5)
resultLabel.pack(pady=5)

## sign up from Firebase function
def addUser(view, accountentry, passwordentry):
    print(accountentry.get(),passwordentry.get())
    print("Signup...")
    # Assign user's entry to parameter account and parameter password.
    account = accountentry.get()
    password = passwordentry.get()
    try:
        user = auth.create_user_with_email_and_password(account, password)
        print("Successfully signup!")
        resultLabel.config(text = "Successfully signup!") # reset label for successfully signup.
    except Exception as e:
        # print("Email account has already exist!")
        # resultLabel.config(text = "Email account has already exist!") # reset label for fail to signup.
        print(f"創建使用者失敗: {e}") # reset label for fail to signup.
        resultLabel["text"] = "Email account has already exist!"

## login from Firebase function 
def verifyUser(view, accountentry, passwordentry):
    print(accountentry.get(),passwordentry.get())
    print("Log in...")
    # Assign user's entry to parameter account and parameter password.
    account = accountentry.get()
    password = passwordentry.get()
    try:
        login = auth.sign_in_with_email_and_password(account, password)
        print(login['localId'])
        print("Successfully logged in!")
        resultLabel.config(text = "Successfully logged in!")# reset label for successfully login.
    except:
        print("Invalid email or password!")
        resultLabel.config(text = "Invalid email or password!")# reset label for successfully login.


root.mainloop()