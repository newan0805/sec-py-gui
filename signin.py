from tkinter import *
from tkinter import messagebox
import ast
import hashlib
import re
import random
from captcha.image import ImageCaptcha
from PIL import ImageTk,Image
import io

def SignIn():
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def is_strong_password(password):
        if len(password) < 8:
            return False

        # Contains at least one lowercase letter
        if not re.search("[a-z]", password):
            return False

        # Contains at least one uppercase letter
        if not re.search("[A-Z]", password):
            return False

        # Contains at least one digit
        if not re.search("[0-9]", password):
            return False

        # Contains at least one special character
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

        # Generate the image captcha
        image = ImageCaptcha(width=280, height=90)
        data = image.generate(expected_captcha)
        image.write(expected_captcha, out_path)

        # Load the saved captcha image using PIL
        captcha_img = Image.open(out_path)
        captcha_img = ImageTk.PhotoImage(captcha_img)

        # Display the image in a Label
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

        # open_captcha_window('generate', 'aa', 'aa')


        if password == confirm_password and is_strong_password(password):
            try:
                # Read existing user data or initialize an empty dictionary
                with open('datasheet.txt', 'r') as file:
                    data = file.read().strip()
                    if data:
                        user_data = ast.literal_eval(data)
                        print(user_data)
                    else:
                        user_data = {}

                # Add the new user data
                user_data[username] = hash_password(password)

                # Generate CAPTCHA
                captcha = generate_captcha()

                # Open CAPTCHA window
                open_captcha_window(captcha, username, password)

            except Exception as e:
                print(f"Error during signup: {e}")
                # Handle file-related errors

        else:
            if password != confirm_password:
                messagebox.showerror('Invalid', 'Both passwords should match')
            else:
                messagebox.showerror('Invalid', 'Please create a stronger password')

    import json

    def record_user(username, password):
        try:
            # Read existing user data or initialize an empty dictionary
            with open('datasheet.txt', 'r') as file:
                data = file.read().strip()
                if data:
                    user_data = json.loads(data)
                else:
                    user_data = {}

            # Add the new user data
            user_data[username] = (password)

            # Write the updated user data back to the file
            with open('datasheet.txt', 'w') as file:
                file.write(json.dumps(user_data))

        except Exception as e:
            print(f"Error recording user: {e}")

    window = Tk()
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    img = PhotoImage(file='./assets/vectors/login.png')
    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='white')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter(e):
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
        code.delete(0, 'end')
        code.config(show='*')

    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')
            code.config(show='')

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    def on_enter(e):
        confirm_code.delete(0, 'end')
        confirm_code.config(show='*')

    def on_leave(e):
        if code.get() == '':
            confirm_code.insert(0, 'Re-enter the Password')
            confirm_code.config(show='')

    confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Re-enter the Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)

    signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
    signin.place(x=200, y=340)

    window.mainloop()
