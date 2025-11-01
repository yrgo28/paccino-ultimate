#!/bin/bash
#PACCINO INSTALLER FOR BASH SHELL BY: yrgo28

git clone https://github.com/yrgo28/paccino-ultimate.git
echo 'export PACCINO_PATH=$HOME/paccino-ultimate' >> $HOME/.bashrc
echo "alias paccino='python3 $PACCINO_PATH/main.py'" >> $HOME/.bashrc

echo 'Paccino has been installed. Type "paccino" to open it.'

#Done.

