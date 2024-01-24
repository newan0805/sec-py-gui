from login import Login as Login
from signin import SignIn as SignIn
from profile import Profile as Profile
# import login as login_form
# import signin as signin_form

# load_login_form()
# load_signin_form()

# login_form()
# signin()

login_attempts = 0;

def mainl():
    e = SignIn()
    if e == 'success':
        Profile()
    else:
        e = Login()
        if e == 'fail':
            Profile()
        login_attempts += 1

print(login_attempts)
mainl()
# if __name__ == "__main__":
#     root = Tk()
#     root.title('Login')
    # Add other configurations...
    
    # Your existing code for creating the login window...
    
    # root.mainloop()


# if __name__ == "__main__":