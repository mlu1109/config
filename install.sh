#!/bin/bash

sudo apt update

echo Setting up git and cloning configs...
sudo apt install -y git

echo Setting up i3
sudo apt install -y i3 i3lock-fancy i3blocks fonts-font-awesome fonts-inconsolata
ln -s i3wm ~/.config/i3

echo Setting up urxvt
sudo apt install -y rxvt-unicode
ln -s .Xresources ~/.Xresources
ln -s .Xresources.d ~/.Xresources.d
xrdb -merge ~/.Xresources
echo xrdb -merge ~/.Xresources >> ~/.profile

echo Setting up zsh
sudo apt install -y zsh
ln -s .zshrc ~/.zshrc

echo Set zsh as default shell
chsh -s $(which zsh)

echo Set default terminal
sudo update-alternatives --config x-terminal-emulator
