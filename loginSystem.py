from stdiomask import getpass
import hashlib
import os
clear = lambda: os.system('cls ')




def main():
    clear()
    print("Main Menu")
    print("-----")
    print("1 - to login")
    print("2 - to Register")

    while True:     
        userChoice = input("Would you like to login or register?")
        if userChoice in ["1", "2"]:
            break    
    if userChoice == "1":
        userLogin()
    else:
        userRegister()





def userRegister():
   print()
   print("REGISTER")
   print("-----")
   print()
   
   while True:
       userName = input("Enter your username: ").title()
       if userName != '':
           break
   userName = sanitizeName(userName)    
   while True:
        passWord = getpass("Enter your password: ")
        if passWord != '':
            break
   while True:
        confirmPassword = getpass("Confirm you password: ")
        if confirmPassword == passWord:
            break
        else:
            print("Passwords do not match.")
            print("")
   if userAlreadyExists(userName, passWord):
        while True:
            print()
            error = input("You Are Already Registered\n\n Press (T) To Try Again\n Press (L) To Login: ").lower()
            if error == "t":
                userRegister()
                break
            elif error == "l":
                userLogin()
                break
   addUserInfo([userName, hash_password(passWord)])

   print()
   print("Registered!")
            
    
       

def userLogin():
    clear()
    print()
    print("LOGIN")
    print("-----")
    print()
    loginDocumentation = {}
    with open('loginDocumentation.txt', 'r') as file:
        for line in file:
            line = line.split()
            loginDocumentation.update({line[0]: line[1]})

    while True:
        userName = input("Enter Your Name: ").title()
        userName = sanitizeName(userName)
        if userName not in loginDocumentation:
            print("Your Are Not Registered.")
            print()
        else:
            break
    while True:
        passWord = getpass("Enter Your Password: ")
        if not check_password_hash(passWord, loginDocumentation[userName]):
            print("Incorrect Password!")
            print()
        else:
            break


    print()
    print("Logged In!")




    
def addUserInfo(loginDocumentation: list):
    with open('loginDocumentation.txt', 'a') as file:
        for info in loginDocumentation:
            file.write(info)
            file.write(' ')
        file.write("\n")

def userAlreadyExists(userName, passWord):
    passWord = hash_password(passWord)
    usersInfo = {}
    with open('loginDocumentation.txt', 'r') as file:
        for line in file:
            line = line.split()
            if line[0] == userName and line[1] == (passWord):
                usersInfo.update({line[0]: line[1]})
    if usersInfo == {}:
        return False
    return usersInfo[userName] == passWord






def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName



def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()



def check_password_hash(password, hash):
    return hash_password(password) == hash 



main()



    







