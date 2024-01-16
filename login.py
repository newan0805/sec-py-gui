from tkinter import *
from tkinter import messagebox
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login():
    username = user_var.get()
    password = password_var.get()

    if username == 'admin' and hash_password(password) == hash_password('1234'):
        messagebox.showinfo('Login Successful', 'Welcome, Admin!')
        open_new_window()  
    else:
        messagebox.showerror('Login Failed', 'Invalid username or password')


def open_new_window():
    new_window = Toplevel(root)
    new_window.title('Welcome')
    new_window.geometry('600x300')
    new_window.configure(bg="#a0d8ff")

    Label(new_window, text='Welcome to the System!', font=('Microsoft YaHei UI Light', 24, 'bold'), bg="#a0d8ff").pack(
        pady=20)
    Label(new_window, text='We are glad to have you on board.', font=('Microsoft YaHei UI Light', 16),
          bg="#a0d8ff").pack(pady=10)
    Button(new_window, text='Logout', command=root.destroy, font=('Microsoft YaHei UI Light', 14), bg="#57a1f8",
           fg='white').pack(pady=20)


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


def on_enter_username(e):
    user.delete(0, 'end')


def on_leave_username(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user_var = StringVar()
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11),
             textvariable=user_var)
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter_username)
user.bind('<FocusOut>', on_leave_username)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_enter_password(e):
    code.delete(0, 'end')
    code.config(show='*')


def on_leave_password(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')
        code.config(show='')


password_var = StringVar()
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11),
             textvariable=password_var)
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter_password)
code.bind('<FocusOut>', on_leave_password)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=login).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white',
              font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
