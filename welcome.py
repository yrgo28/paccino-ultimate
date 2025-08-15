import os

class ascii:
    def __init__(self):
        pass
    
    def print_ascii(self):
        comm = 'printf "\e[32m$(< $PACCINO_PATH/ascii_art)\e[0m\n"'
        os.system(comm)
        print(" ")

