#!/bin/python3

import os
import termcolor
from termcolor import colored
from datetime import date

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

def history(put: str):
    interact._exec(f'echo {date.today()}: {put} >> $PACCINO_PATH/history.txt')

class Sync():
    def __init__(self):
        pass

    def Install(self, mode: str):
        modes_avail = ["-S", "-Syu", "-U", "aur"]
        #     0 = normal; 1 = seguro; 2 = desde archivo

        if(mode=="aur"):
            new_menu("aur")
        else:
            new_menu("install")

        package = input("Package name: ")
        if(len(package) > 1 and mode in modes_avail and mode != "aur"):
            new_menu("installing")
            interact._exec(f"sudo pacman {mode} {confirmation} {package}")
            history(f'Installed from pacman: {package}')
        elif(len(package) > 1 and mode in modes_avail and mode == "aur"):
            ui.clear()
            print(f"Installing from AUR.")
            ui.separator("line")
            interact._exec(f"yay -S {package}")
            history(f'Installed from AUR: {package}')
        else:
            pass

    def Synchronize(self, mode: str):
        avail = ["-Syu", "-Syyu"]
        #########NORMAL ; FORZADA

        new_menu("sync")
        if(mode in avail):
            new_menu("synchronizing")
            interact._exec(f"sudo pacman {mode} {confirmation}")
            history(f'Synchronized.')
        else:
            pass

class Remove():
    def __init__(self, mode: str):
        mode = mode
        
        new_menu("remove")
        package = input("Package name: ")
        if(len(package) > 1):
            new_menu("removing")
            interact._exec(f"sudo pacman {mode} {confirmation} {package}")
            history(f'Removed: {package}')
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
        if(len(user_type) > 1):
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
        history(f'Cache cleaned.')
        interact._exec(f"sudo pacman -Scc")
        ui.separator("enter")
        avail = ["y", "n"]
        quest = input('Remove yay cache files? (y/n): ')

        if(quest in avail):
            if(quest=="y"):
                print(colored("waiting for removing $HOME/.cache/yay/*", "yellow"))
                cons = input("Continue? (y/n): ")
                if(cons == "y"):
                    history(f'yay cache cleaned.')
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

        if(rcfile.default_text_editor!=None):
            interact._exec(f'{rcfile.default_text_editor} $PACCINO_PATH/rcfile.py')
            ui.separator("enter")
            print("info: rcfile has been modified.")
            ui.separator("enter")
        else:
            ui.separator("enter")
            interact._exec(f'echo edit "rcfile.py" in $PACCINO_PATH')
            ui.separator("enter")
            print(colored("Use vim, nano or any text editor.", "yellow"))
        # 3

    def history(self):
        new_menu("history")
        interact._exec(f'cat $PACCINO_PATH/history.txt')
        ui.separator("enter")
        print(colored('history is stored in $PACCINO_PATH/history.txt', "yellow"))

    def pacman_conf(self):
        new_menu("no title")

        if(rcfile.default_text_editor!=None):
            interact._exec(f'{rcfile.default_text_editor} /etc/pacman.conf')
            ui.separator("enter")
            print('info: pacman.conf has been modified.')
            ui.separator("enter")
            #interact._exec(f'{rcfile.default_text_editor} {rcfile.pacman_config_dir}') # ---> Uncomment this if you have a custom path for pacman.conf
        else:
            ui.separator("enter")
            print(colored("info: Use any text editor for edit /etc/pacman.conf."))
            ui.separator("enter")

    def credits(self):
        new_menu("no title")
        interact._exec(f"cat $PACCINO_PATH/credits.paccino")
        # 99

