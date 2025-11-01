import os
import termcolor
from termcolor import colored
import welcome
import rcfile

rc = rcfile

def terminal_size():
    num = os.get_terminal_size().columns
    return num

class UI:
    def __init__(self):
        pass

    def header(self, arg: str):
        avail = ["main", "more", "install", "remove", "search", "advanced", "sync", "info", "no title", "aur", "synchronizing", "installing", "removing", "history"]

        welcome.ascii().print_ascii()
        if(arg in avail):
            if(arg=="main"):
                print("Main menu.")
                
            elif(arg=="more"):
                print("Other options.")
                
            elif(arg=="install"):
                print("Install new package.")
                
            elif(arg=="remove"):
                print("Remove packages.")
                
            elif(arg=="search"):
                print("Search a package.")
                
            elif(arg=="advanced"):
                print("Advanced mode menu.")

            elif(arg=="sync"):
                print("Synchronize modes.")

            elif(arg == "info"):
                print("Information functions.")

            elif(arg == "aur"):
                print(f'Install from AUR.')

            elif(arg == "synchronizing"):
                print('Synchronizing.')

            elif(arg == "installing"):
                print('Installing a new Package.')

            elif(arg == "removing"):
                print('Removing a Package.')

            elif(arg == "history"):
                print("History.")

            elif(arg=="no title"):
                pass
        else:
            print("Error: Header not found.")

    def clear(self):
        os.system("clear")
    
    def separator(self, separator_type: str):
        types = ["enter", "line"]
        if(separator_type in types):
            pass
        elif(separator_type not in types or separator_type == None):
            separator_type = "enter"

        if(separator_type == "line"):
            print(rc.separator_line_char * terminal_size())
        elif(separator_type == "enter"):
            print(" ")

class Interact:
    def __init__(self):
        pass
    
    def enter_to_continue(self):
        cons = input("Type [ENTER] to continue...")

    def _exec(self, arg):
        os.system(arg)


