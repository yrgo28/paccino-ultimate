#!/bin/python3

import os
import termcolor
from termcolor import colored

import func
import backend
import rcfile

ui = func.UI()
interact = func.Interact()
sync = backend.Sync()
info = backend.Info()
more = backend.More()
adv = backend

# CODE FORMAT
# choose_<mode> / eg: choose function for main menu is: choose_main()
# menu_<menu> / eg: function for install menu is: menu_install()

# CHOOSE BLOCK

def choose_more():
    avail = ["00", "1", "2", "3", "4", "5"] #ADD "99" for credits (unused)
    choose = input("Type your option: ")

    while True:
        if(choose in avail):
            ui.separator("line")
            
            if(choose == "00"):
                menu_main()

            if(choose == "1"):
                more.remove_unused()

            elif(choose == "2"):
                more.cache_clean()

            elif(choose == "3"):
                more.edit_rc()

            elif(choose == "4"):
                more.history()

            elif(choose == "5"):
                more.pacman_conf()

            elif(choose == "99"):
                more.credits()

            ui.separator("line")
            interact.enter_to_continue()

        menu_more()

def choose_search():
    avail = ["00", "1", "2", "3"]
    choose = input("Type your option: ")

    while True:
        ui.separator("line")

        if(choose in avail):
            if(choose == "00"):
                menu_main()

            if(choose == "1"):
                info.search("pacman")
            elif(choose == "2"):
                info.search("aur")
            elif(choose == "3"):
                info.search("installed")

            ui.separator("line")
            interact.enter_to_continue()

        menu_search()

def choose_info():
    avail = ["00", "1", "2"]
    choose = input("Type your option: ")

    while True:
        ui.separator("line")
        if(choose in avail):
            if(choose == "00"):
                menu_main()

            if(choose == "1"):
                info.list_installed()

            elif(choose == "2"):
                info.properties()
            
            ui.separator("line")
            interact.enter_to_continue()

        menu_info()

def choose_sync():
    avail = ["1", "2", "00"]
    choose = input("Type your option: ")

    while True:
        ui.separator("line")
        if(choose in avail):
            if(choose == "00"):
                menu_main()

            if(choose == "1"):
                sync.Synchronize("-Syu")
            elif(choose == "2"):
                sync.Synchronize("-Syyu")

            ui.separator("line")
            interact.enter_to_continue()

        menu_sync()

def choose_install():
    avail = ["1", "2", "3", "4", "00"]
    choose = input("Type your option: ")

    while True:
        ui.separator("line")
        if(choose in avail):
            if(choose == "00"):
                menu_main()

            if(choose == "1"):
                sync.Install("-S")
            elif(choose == "2"):
                sync.Install("-Syu")
            elif(choose == "3"):
                sync.Install("aur")
            elif(choose == "4"):
                sync.Install("-U")

            ui.separator("line")
            interact.enter_to_continue()

        menu_install()

def choose_remove():
    avail = ["00", "1", "2", "3"]
    choose = input("Type your option: ")

    while True:
        if(choose in avail):
            if(choose == "00"):
                menu_main()

            if(choose == "1"):
                adv.Remove("-R")
            elif(choose == "2"):
                adv.Remove("-Rs")
            elif(choose == "3"):
                adv.Remove("-Rns")
                
            ui.separator("line")
            interact.enter_to_continue()
        

        menu_remove()

def choose_main():
    avail = ["1", "2", "3", "4", "5", "6"]
    exit_modes = ["q", "exit", "quit", "00", "Q"]
    choose = input("Type your option: ")

    if(choose in exit_modes):
        ui.clear()
        exit()
    
    while True:
        if(choose in avail):
            if(choose=="1"):
                menu_sync()

            elif(choose == "2"):
                menu_install()

            elif(choose == "3"):
                menu_remove()

            elif(choose == "4"):
                menu_info()

            elif(choose == "5"):
                menu_search()

            elif(choose == "6"):
                menu_more()

        menu_main()

# END CHOOSE BLOCK

# MENU BLOCK

# FORMAT
# CLEAR THE SCREEN > TYPE MENU TITLE > PRINT OPTIONS
# format is number per option
# eg: 1 for start > [1] Start

def menu_main():
    ui.clear()
    ui.header("advanced")
    ui.separator("line")

    if(rcfile.show_main_menu_info):
        print(f"help: Type option number and press [enter] to get in.")
        print(f"e.g: 2 > Install.")
        ui.separator("enter")
    else:
        pass

    if(rcfile.show_pkg_installed):
        interact._exec('printf "Installed Packages: $(pacman -Q | wc -l) \n"')
        ui.separator("enter")
    else:
        pass

    print(colored("[1] Synchronize", "yellow"))
    print(colored("[2] Install", "cyan"))
    print(colored("[3] Remove", "blue"))
    print(colored("[4] Information", "green"))
    print(colored("[5] Search", "cyan"))
    print(colored("[6] More", "magenta"))
    ui.separator("enter")
    print(colored("[00] Quit", "red"))
    ui.separator("line")
    choose_main()

def menu_install():
    ui.clear()
    ui.header("install")
    ui.separator("line")
    print(colored("[1] From Database", "green")) # -S
    print("info: Type package name, download and install it.")
    ui.separator("enter")
    print(colored("[2] Secure Mode", "cyan")) # -Syu
    print("info: Synchronize databases before installation.")
    ui.separator("enter")
    print(colored("[3] From AUR", "cyan"))
    print(f"info: Install any package from AUR repository.")
    ui.separator("enter")
    print(colored("[4] From File", "yellow")) # -U
    print("info: Type /path/to/file.pkg.tar.zst or file name (fetched in cache), and install it.")
    ui.separator("enter")
    print(colored("[00] Back", "blue"))
    ui.separator("line")
    choose_install()

def menu_sync():
    ui.clear()
    ui.header("sync")
    ui.separator("line")
    print(colored("[1] Normal", "green"))
    print("info: Comprobe updates from databases and install it.")
    ui.separator("enter")
    print(colored("[2] Forced", "cyan"))
    print("info: Force refresh of Databases.")
    ui.separator("enter")
    print("note: After an update/upgrade, system reboot is highly recommended.")
    ui.separator("enter")
    print(colored("[00] Back", "blue"))
    ui.separator("line")
    choose_sync()

def menu_remove():
    ui.clear()
    ui.header("remove")
    ui.separator("line")
    print(colored("[1] Normal Remove", "magenta"))
    print("info: Type package name and remove it.")
    ui.separator("enter")
    print(colored("[2] Advanced Remove", "green"))
    print("info: Remove package and unused dependences.")
    ui.separator("enter")
    print(colored("[3] Purge", "yellow"))
    print("info: Remove package, dependences and configuration files.")
    ui.separator("enter")
    print(colored("[00] Back", "blue"))
    ui.separator("line")
    choose_remove()

def menu_info():
    ui.clear()
    ui.header("info")
    ui.separator("line")
    print(colored("[1] List Installed", "green"))
    print(f"info: Show a list of all installed packages.")
    ui.separator("enter")
    print(colored("[2] Package Properties", "green"))
    print(f"info: Type package-name and show they properties.")
    ui.separator("enter")
    print(colored("[00] Back", "blue"))
    ui.separator("line")
    choose_info()

def menu_search():
    ui.clear()
    ui.header("search")
    ui.separator("line")
    print(colored("[1] Search in Database", "green"))
    print(f"info: Type packages and show concidences.")
    ui.separator("enter")
    print(colored("[2] Search in AUR", "cyan"))
    print(f"info: Show concidences in AUR repository for yay.")
    ui.separator("enter")
    print(colored("[3] Search in Installed", "green"))
    print(f"info: Type package name and comprobe if it's installed.")
    ui.separator("enter")
    print(colored("[00] Back", "blue"))
    ui.separator("line")
    choose_search()

def menu_more():
    ui.clear()
    ui.header("more")
    ui.separator("line")
    print(colored("[1] Remove Unused", "magenta"))
    print(f"info: Show and remove unused dependences/packages.")
    ui.separator("enter")
    print(colored("[2] Cache Clean", "yellow"))
    print(f"info: pacman/yay cache clean wizard.")
    ui.separator("enter")
    print(colored("[3] Edit RCFile", "cyan"))
    print(f"info: Edit paccino's configuration file. (Restart needed)")
    ui.separator("enter")
    print(colored("[4] History", "green"))
    print("info: Displays a list of the actions that have been performed.")
    ui.separator("enter")
    print(colored("[5] Edit pacman.conf", "red"))
    print("info: edit the pacman's configuration file.")
    ui.separator("enter")
    print(colored("[00] Back", "blue"))
    ui.separator("line")
    choose_more()

# END MENU BLOCK

# START
# Paccino will be started on main menu by default
# customized starts IS NOT recommended

menu_main()

# END

