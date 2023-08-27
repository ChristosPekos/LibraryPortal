from functionslib import *


def menu():
    
    print("Welcome to our School's library portal")
    login_or_signup = input("Choose the number of the action you want to take:\n(1)Log in\n(2)Sign up\n")
    
    if login_or_signup == '1':
        login()
    else:
        signup()
 


if __name__ == '__main__':
    menu()

