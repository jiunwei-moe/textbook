#!/bin/bash

if [ -d ~/.virtualenvs/textbook ]; then
	echo "Environment already set up. Exiting..."
	exit
fi

echo "Installing virtualenv..."
sudo pip install virtualenv

echo "Installing virtualenvwrapper..."
sudo pip install virtualenvwrapper

echo "Editing .bashrc..."
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo 'export PROJECT_HOME=$HOME/workspace' >> ~/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source .bashrc

echo "Installing python packages..."
source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv -a . -r requirements.txt -p python3 textbook

echo "Installing ImageMagick..."
sudo add-apt-repository main
sudo apt-get update
sudo apt-get install imagemagick

echo "Installing pandoc..."
wget https://github.com/jgm/pandoc/releases/download/1.16.0.2/pandoc-1.16.0.2-1-amd64.deb
sudo dpkg -i pandoc-1.16.0.2-1-amd64.deb
sudo apt-get install -f

echo "Done!"
