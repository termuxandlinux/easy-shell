#!/bin/bash

# Ask the user which browser they want to install
read -p "Which browser would you like to install? Enter 'firefox', 'konqueror' or 'tor': " browser

# Check the user input and install the corresponding browser
if [ "$browser" = "firefox" ]; then
    apt install firefox
elif [ "$browser" = "konqueror" ]; then
    apt install konqueror
elif [ "$browser" = "tor" ]; then
    apt install tor
else
    echo "Invalid input. Please enter 'firefox', 'konqueror' or 'tor'."
fi