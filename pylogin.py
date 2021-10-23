import os
import sys
import create

#########################PRINT COLORS################################
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLGray(skk): print("\033[97m {}\033[00m" .format(skk))
####################################################################


# GET THE MAIN VARIABLES


prGreen(" ___________________________________________")
prGreen("|                                           |")
prGreen("|       PLEESE ANSWER THE QUESTIONS         |")
prGreen("|                                           |")
prGreen("|                                           |")
prGreen("|                                           |")
prGreen("|                                           |")
prGreen("|                                           |")
prGreen("|___________________________________________|")
print("\n\n\n")


def akp():
    print("_____________________________________________")
    print("|                                           |")
    print("| PLEESE INSERT YOUR Firebase apiKey        |")
    print("|___________________________________________|")
    global apikey
    apikey = input(" => ")
    print("\n\n\n")


def audp():
    print("_____________________________________________")
    print("|                                           |")
    print("| PLEESE INSERT YOUR Firebase authDomain    |")
    print("|___________________________________________|")
    global authDom
    authDom = input(" => ")
    print("\n\n\n")


def pip():
    print("_____________________________________________")
    print("|                                           |")
    print("| PLEESE INSERT YOUR Firebase projectId     |")
    print("|___________________________________________|")
    global projId
    projId = input(" => ")
    print("\n\n\n")


def sbp():
    print("_____________________________________________")
    print("|                                           |")
    print("| PLEESE INSERT YOUR Firebase storageBucket |")
    print("|___________________________________________|")
    global storageBuck
    storageBuck = input(" => ")
    print("\n\n\n")


def msip():
    print("_________________________________________________")
    print("|                                               |")
    print("| PLEESE INSERT YOUR Firebase messagingSenderId |")
    print("|_______________________________________________|")
    global messagingSenderId
    messagingSenderId = input(" => ")
    print("\n\n\n")


def faip():
    print("_____________________________________________")
    print("|                                           |")
    print("| PLEESE INSERT YOUR Firebase appId         |")
    print("|___________________________________________|")
    global appId
    appId = input(" => ")
    print("\n\n\n")


# Call the main functions
akp()
audp()
sbp()
pip()
msip()
faip()

prGreen(" _________________________________________________________")
prGreen("|")
prGreen(f"|   Api Key:              {apikey}")
prGreen(f"|   Auth Domain:          {authDom}")
prGreen(f"|   Project ID:           {projId}")
prGreen(f"|   Storage Bucket:       {storageBuck}")
prGreen(f"|   Menssage Sender ID:   {messagingSenderId}")
prGreen(f"|   App ID:               {appId}")
prGreen("|__________________________________________________________")
print("\n")

prRed("Is this information corect?(yes/no)")
correctinfchoice = input(" => ")

def fcc():
    # Call the main functions
    akp()
    audp()
    sbp()
    pip()
    msip()
    faip()

    prGreen(" _________________________________________________________")
    prGreen("|")
    prGreen(f"|   Api Key:              {apikey}")
    prGreen(f"|   Auth Domain:          {authDom}")
    prGreen(f"|   Project ID:           {projId}")
    prGreen(f"|   Storage Bucket:       {storageBuck}")
    prGreen(f"|   Menssage Sender ID:   {messagingSenderId}")
    prGreen(f"|   App ID:               {appId}")
    prGreen("|__________________________________________________________")
    print("\n")

    prRed("Is this information corect?(yes/no)")
    correctinfchoice = input(" => ")

    if correctinfchoice == "yes":
        pro=create.CreateFirebase()
        pro.checkre()
        pro.createFirebase(apikey, authDom, projId, storageBuck, messagingSenderId, appId)
    elif correctinfchoice == "no":
        fcc()
    else:
        prRed("UNKNOW OPTION")
        fcc()

if correctinfchoice == "yes":
    pro=create.CreateFirebase()
    pro.checkre()
    pro.createFirebase(apikey, authDom, projId, storageBuck, messagingSenderId, appId)

    prGreen(" ___________________________________________")
    prGreen("|                                           |")
    prGreen("|       NOW THE Pylog JavaScript SOUCE      |")
    prGreen("|       IS READY.                           |")
    prGreen("|       SO PUT YOUR PROJECT IN THE LINK     |")
    prGreen("|       TAG ON index.js LOCATED ON          |")
    prGreen("|       log/src/                            |")
    prGreen("|                                           |")
    prGreen("|___________________________________________|")
    print("\n\n\n")
    sys.exit()

elif correctinfchoice == "no":
    fcc()
else:
    prRed("UNKNOW OPTION")
    fcc()
