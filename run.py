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
