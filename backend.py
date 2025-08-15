#!/bin/python3

import os
import termcolor
from termcolor import colored

import func
import rcfile

ui = func.UI()
interact = func.Interact()
rc = rcfile

# wait confirmation control

confirmation: str

if(rc.wait_confirmation==False):
    confirmation = "--noconfirm"
else:
    confirmation = ""

# START

def new_menu(header_type: str):
    ui.clear()
    ui.header(header_type)
    ui.separator("line")

class Sync():
    def __init__(self):
        pass

    def Install(self, mode: str):
        modes_avail = ["-S", "-Syu", "-U", "aur"]
        #     0 = normal; 1 = seguro; 2 = desde archivo

        new_menu("install")
        package = input("Package name: ")
        if(len(package) > 2 and mode in modes_avail and mode != "aur"):
            interact._exec(f"sudo pacman {mode} {confirmation} {package}")
        elif(len(package) > 2 and mode in modes_avail and mode == "aur"):
            ui.clear()
            print(f"Installing from AUR.")
            ui.separator("line")
            interact._exec(f"yay -S {package}")
        else:
            pass

    def Synchronize(self, mode: str):
        avail = ["-Syu", "-Syyu"]
        #########NORMAL ; FORZADA

        new_menu("sync")
        if(mode in avail):
            interact._exec(f"sudo pacman {mode} {confirmation}")
        else:
            pass

class Remove():
    def __init__(self, mode: str):
        mode = mode
        
        new_menu("remove")
        package = input("Package name: ")
        if(len(package) > 2):
            interact._exec(f"sudo pacman {mode} {confirmation} {package}")
        else:
            pass

class Info():
    def __init__(self):
        pass

    def list_installed(self):
        new_menu("no title")
        interact._exec(f"pacman -Qq | column")

    def properties(self):
        new_menu("no title")
        user_type = input("Package name: ")
        ui.separator("line")
        interact._exec(f"pacman -Qii | grep {user_type}")

    def search(self, mode: str):
        new_menu("search")
        user_type = input("Search: ")
        if(len(user_type) > 2):
            ui.separator("line")
            if(mode=="pacman"):
                interact._exec(f"pacman -Ssq {user_type} | column | column")
            elif(mode=="aur"):
                interact._exec(f"yay -Ssq {user_type} | column | column")
            elif(mode=="installed"):
                interact._exec(f"pacman -Q | grep '{user_type}' | column")
        else:
            pass

class More():
    def __init__(self):
        pass

    def cache_clean(self):
        new_menu("no title")
        interact._exec(f"sudo pacman -Scc")
        ui.separator("enter")
        avail = ["y", "n"]
        quest = input('Remove yay cache files? (y/n): ')

        if(quest in avail):
            if(quest=="y"):
                print(colored("waiting for removing $HOME/.cache/yay/*", "yellow"))
                cons = input("Continue? (y/n): ")
                if(cons == "y"):
                    ui.separator("enter")
                    interact._exec(f"sudo rm -rf $HOME/.cache/yay/*")
                    print(f"yay cache has been cleaned.")
                else:
                    pass
        else:
            pass
        # 2

    def remove_unused(self):
        new_menu("no title")
        interact._exec(f"sudo pacman -Rns {confirmation} $(pacman -Qtdq)")
        # 1

    def edit_rc(self):
        new_menu("no title")
        interact._exec(f'echo edit "rcfile.py" in $PACCINO_PATH')
        ui.separator("enter")
        print(colored("Use vim, nano or any text editor.", "yellow"))
        # 3

    def credits(self):
        new_menu("no title")
        interact._exec(f"cat $PACCINO_PATH/credits.paccino")
        # 4

