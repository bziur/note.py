#!/bin/bash
sudo cp ./note.py /usr/local/lib/note/note.py &&
sudo chmod +x /usr/local/lib/note/note.py &&
sudo ln /usr/local/lib/note/note.py /usr/local/bin/note  &&
sudo chmod +x /usr/local/bin/note &&
mkdir ~/Documents/notes &&
echo "* add something" >> ~/Documents/notes/todo.txt &&
echo "note -p" >> ~/.bashrc;

