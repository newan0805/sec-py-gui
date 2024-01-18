from tkinter import *
from tkinter import messagebox
import ast
import hashlib
import re
import random
from captcha.image import ImageCaptcha
from PIL import ImageTk,Image
import io
import json


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_strong_password(password):
    if len(password) < 8:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True

def generate_captcha():
    captcha_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    captcha_length = 6
    captcha = ''.join(random.choice(captcha_characters) for _ in range(captcha_length))
    return captcha

def verify_captcha(entered_captcha, expected_captcha):
    return entered_captcha == expected_captcha

def open_captcha_window(expected_captcha, username, password):
    print("Captcha:", expected_captcha)
    captcha_window = Toplevel(window)
    captcha_window.title("CAPTCHA Verification")
    captcha_window.geometry('400x300')
    captcha_window.resizable(False, False)

    captcha_label = Label(captcha_window, text='Enter CAPTCHA:', font=('Arial', 12))
    captcha_label.pack(pady=10)

    out_path = "./captcha.png"

    image = ImageCaptcha(width=280, height=90)
    data = image.generate(expected_captcha)
    image.write(expected_captcha, out_path)

    captcha_img = Image.open(out_path)
    captcha_img = ImageTk.PhotoImage(captcha_img)

    captcha_image_label = Label(captcha_window, image=captcha_img)
    captcha_image_label.image = captcha_img
    captcha_image_label.pack()

    captcha_entry = Entry(captcha_window, width=15, font=('Arial', 12))
    captcha_entry.pack(pady=10)

    verify_button = Button(captcha_window, text='Verify',
                           command=lambda: verify_captcha_callback(captcha_window, captcha_entry.get(),
                                                                   expected_captcha, username, password))
    verify_button.pack(pady=10)
def verify_captcha_callback(captcha_window, entered_captcha, expected_captcha, username, password):
    if verify_captcha(entered_captcha, expected_captcha):
        messagebox.showinfo('CAPTCHA', 'CAPTCHA verification successful!\nSuccessfully Signed Up')
        captcha_window.destroy()
        record_user(username, password)
    else:
        messagebox.showerror('CAPTCHA', 'Incorrect CAPTCHA. Please try again.')

def signup():

    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()
    if password == confirm_password and is_strong_password(password):
        try:
            with open('datasheet.json', 'r') as file:
                data = file.read().strip()
                if data:
                    user_data = ast.literal_eval(data)
                    print(user_data)
                else:
                    user_data = {}

            user_data[username] = hash_password(password)
            captcha = generate_captcha()
            open_captcha_window(captcha, username, password)
        except Exception as e:
            print(f"Error during signup: {e}")
    else:
        if password != confirm_password:
            messagebox.showerror('Invalid', 'Both passwords should match')
        else:
            messagebox.showerror('Invalid', 'Please create a stronger password')

def record_user(username, password):
    try:
        with open('datasheet.json', 'r') as file:
            data = file.read().strip()
            if data:
                user_data = json.loads(data)
            else:
                user_data = {}
        user_data[username] = (password)
        with open('datasheet.json', 'w') as file:
            file.write(json.dumps(user_data))

    except Exception as e:
        print(f"Error recording user: {e}")

def toggle_password_visibility(entry_widget, view_button):
    if entry_widget.cget("show") == "*":
        entry_widget.config(show="")
        view_button.config(text="Hide Password")
    else:
        entry_widget.config(show="*")
        view_button.config(text="View Password")
        
def close_window():
    window.destroy()

window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
# window.attributes("-alpha", 0.9)
# window.overrideredirect(1)

# close_image = Image.open("./assets/icons/close_white.png")
# close_image = ImageTk.PhotoImage(close_image)

# eye_open_image = Image.open("./assets/icons/view.png")
# eye_open_image = ImageTk.PhotoImage(eye_open_image) 

# eye_closed_image = Image.open("./assets/icons/hide.png")
# eye_closed_image = ImageTk.PhotoImage(eye_closed_image)

# title_bar = Frame(window, bg='white', relief='raised', bd=2, width=350, height=3)
# title_bar.pack(fill=X)

# close_button = Button(title_bar, text='X', command=close_window)
# close_button.pack(side=RIGHT)
# close_button = Button(title_bar, image=close_image, command=close_window)
# close_button = Button(title_bar,  command=close_window)
# close_button.pack(side=RIGHT)

# bg_img = Image.open("./assets/vectors/peakpx.png")
# # bg_img = bg_img.resize((300, 200), Image.LANCZOS)
# bg_img = ImageTk.PhotoImage(bg_img)
# Label(window, image=bg_img).pack()

img = Image.open("./assets/vectors/signup.png")
# img = ImageTk.PhotoImage(img)
# img = img.resize((300, 100), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
# img = img.pack()
Label(window, image=img, border=0, bg='white').place(x=50, y=50)

frame = Frame(window, width=350, height=390, bg='white')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    # if user.get() == 'Username':
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    # if code.get() == 'Password':
        code.delete(0, 'end')   
        code.config(show='*')

def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show='')
        
code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

def on_enter(e):
    # if confirm_code.get() == 'Re-enter the Password':
    confirm_code.delete(0, 'end')
    confirm_code.config(show='*')

def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Re-enter the Password')
        confirm_code.config(show='')

def load_login_form():
    login_window = Toplevel(window)
    login_window.title("Login")

confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Re-enter the Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=300)
label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Login', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=load_login_form)
signin.place(x=200, y=340)

# confirm_view_password_button = Button(frame, text="View Password", command=lambda: toggle_password_visibility(confirm_code, confirm_view_password_button))
# confirm_view_password_button.place(x=40, y=260)

window.mainloop()
