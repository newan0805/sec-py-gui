def Profile():
    print("Profile!")
    new_window = Toplevel(root)
    new_window.title('Welcome')
    new_window.geometry('600x300')
    new_window.configure(bg="#a0d8ff")

    Label(new_window, text='Welcome to the System!', font=('Microsoft YaHei UI Light', 24, 'bold'), bg="#a0d8ff").pack(pady=20)
    Label(new_window, text='We are glad to have you on board.', font=('Microsoft YaHei UI Light', 16),bg="#a0d8ff").pack(pady=10)
    Button(new_window, text='Logout', command=root.destroy, font=('Microsoft YaHei UI Light', 14), bg="#57a1f8",fg='white').pack(pady=20)