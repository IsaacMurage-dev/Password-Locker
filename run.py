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
            username = input("Enter your preffered username:")
            password = input("Enter your preffered  password:")
            saveUser(createUser(username, password))
            print(f"Hello {username} thank you for creating your password locker account, you can now proceed")
            print("\n")