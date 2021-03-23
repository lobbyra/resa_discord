#!/bin/bash

# Fresh start

cd src
rm -rf ts.json cookie.txt token.txt response.log &> /dev/null
cd ..

# Check if you have python3

python3 --version &> /dev/null

if [[ $? == 127 ]]
then
	echo "Please install python3 before launch the server."
	exit 1
fi

# Check if you have pip3

pip3 --version &> /dev/null

if [[ $? == 127 ]]
then
	echo "Please install pip3 before launch the server."
	exit 1
fi

# Install dependancies packages

echo "Installing requirements for this script.."

pip3 install -r requirements.txt &> /dev/null

echo "Well done ! All is in your computer !\n"

echo -n "Enter your Discord Bot token $> "

read token

echo -n $token > ./src/token.txt

echo -n "Enter your reservation cookie $> "

read cookie

echo -n $cookie > ./src/cookie.txt
