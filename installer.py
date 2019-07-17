# coding = utf-8
# using namespace std
from datacore.installer_screens import MainInstallerScreen
from datacore.gitter import GitterScreens
from os import system


__help__ = """"""


while True:
    cleaner = system("cls")
    del cleaner
    while True:
        print("""
[1] Installer System.
[2] Gitter System.
[3] Help.
[4] Exit
        """)
        opc = int(input(">>> "))
        confirm = int(input("Confirm?\n[1]Y\n[2]\n>>> "))
        if confirm == 1: break
    if opc == 1:
        try:
            MainInstallerScreen()
        except MainInstallerScreen.EndUsage:
            continue
    elif opc == 2:
        try:
            GitterScreens()
        except GitterScreens.EndUsage:
            continue
    elif opc == 3:
        print(__help__)
        input("<<press any button to return>>")
        continue
    elif opc == 4:
        exit(0)
    else:
        print("That's not a valid option!\nTry't again!")
        continue


