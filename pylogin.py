import os
import sys


class CreateFirebase():
    def checkre(self):
       #########################PRINT COLORS################################
       def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
       def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
       def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
       def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
       def prLGray(skk): print("\033[97m {}\033[00m" .format(skk))
       ####################################################################

       prRed("\n\n")
       prGreen("CHECKING DEPENDENCIES: ")
       print("\n\n")
       prRed("DO YOU ALREDY INSTALLED FIREBASE(yes/no)?")
       checkan=input(" => ")

       def chf(arg):
           if checkan == "yes":
               prGreen("OK...")
           elif checkan == "no":
               prCyan("INSTALLING DEPENDENCIES: ")
               prCyan("npm i firebase")
               os.system("npm i firebase")
               prGreen("\n\nDEPENDENCIES --> OK")
           else:
               chf()

       if checkan == "yes":
           prGreen("OK...")
       elif checkan == "no":
           prCyan("INSTALLING DEPENDENCIES: ")
           prCyan("npm i firebase")
           os.system("npm i firebase")
           prGreen("\n\nDEPENDENCIES --> OK")
       else:
           chf()


    def createFirebase(self, ak, ad, pi, sb, msi, ai):
        #########################PRINT COLORS################################
        def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
        def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
        def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
        def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
        def prLGray(skk): print("\033[97m {}\033[00m" .format(skk))
        ####################################################################

        print("\n\n\n")
        prRed("GETING THE Pylog SOURCE...")
        prYellow("git clone https://github.com/jazzman07/log.git")
        os.system("git clone https://github.com/jazzman07/log.git")

        prCyan("WRITING firebase.js...")

        f = open("log/src/firebase.js", "a")
        f.write("""import firebase from "firebase/compat/app" """)
        f.write("\n")
        f.write("""import "firebase/compat/auth" """)
        f.write("""\n\n""")
        f.write("""const app = firebase.initializeApp({ \n""")
        f.write(f"""      apiKey: '{ak}', \n""")
        f.write(f"""      authDomain: '{ad}', \n""")
        f.write(f"""      projectId: '{pi}', \n""")
        f.write(f"""      storageBucket: '{sb}', \n""")
        f.write(f"""      messagingSenderId: '{msi}', \n""")
        f.write(f"""      appId: '{ai}' \n""")
        f.write(""" \n""")
        f.write("""}) \n""")
        f.write(""" \n""")
        f.write(""" \n""")
        f.write("""export const auth = app.auth() \n""")
        f.write("""export default app \n""")

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
        pro=CreateFirebase()
        pro.checkre()
        pro.createFirebase(apikey, authDom, projId, storageBuck, messagingSenderId, appId)
    elif correctinfchoice == "no":
        fcc()
    else:
        prRed("UNKNOW OPTION")
        fcc()

if correctinfchoice == "yes":
    pro=CreateFirebase()
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
