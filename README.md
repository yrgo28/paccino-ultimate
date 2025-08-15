"Pacinno" is a frontend for "pacman" package manager with "yay" support (from the AUR repository). It's minimalistic: type the number with the option you want to run and press Enter.

It has several options for easy management, such as update options (normal, forced, etc.), list of installed packages, search in repositories, and more...

It's perfect for beginners in the Arch Linux and derivatives community.

/thanks for use paccino <3

**# HOW TO INSTALL**
1. Clone this repository
2. Edit your shell rc file (eg: for bash, nano (or your prefered text editor) $HOME/.bashrc)
3. Type following lines:

* export PACCINO_PATH=/directory/where/you/have/cloned/this/repository (eg: $HOME/paccino-ultimate)
  
* alias paccino='python3 $PACCINO_PATH/main.py'

4. Done!
