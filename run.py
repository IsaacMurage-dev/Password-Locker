from user import User
from credential import Credentials
from random import randint
'''for the user class'''
def createUser(username, password):
    myUser = User(username, password)
    return myUser
def saveUser(user):
    user.saveUser()
def displayUsers():
    User.displayUsers()
    '''this is for the credentials class'''
def createCredentials(account, user_name, pass_word):
    myCred = Credentials(account, user_name, pass_word)
    return myCred

def saveCredentials(credentials):
    credentials.saveCred()
def displayCredentials():
    Credentials.displayCredentials()

def main():
    print("Welcome to your password locker,")
    print("\n")
    while True: 
        shortcodes= input("To create Account,type either cu or du: cu to create user : du to display user:").lower()
        if shortcodes == "cu":
            username = input("Enter your username:")
            password = input("Enter your password:")
            saveUser(createUser(username, password))
            print(f"Hello {username} your password locker account has been created, you can now proceed")
            print("\n")

            while True:
                print(f"Welcome {username} to the section of adding accounts and their passwords:")
                print("-"*20)
                code =input("Please choose the following to interact with the application:  cc: to create credentials: dc to display credentials:").lower()
                if code == "cc":
                    feedback = input("Enter y to create your own password and n for the system to generate:").lower()
                    if feedback == ("y"):
                        account = input("Enter the name of account, eg facebook, twitter:")
                        user_name = input("Enter your desired username:")
                        pass_word = input("Enter the password:")
                        saveCredentials(createCredentials(account,user_name, pass_word))
                        print("Credentials uploaded successfully")

main()