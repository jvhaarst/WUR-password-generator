#!/usr/bin/python
import sys
from random import choice as randomChoice
import re
global passData
global password

passData = [	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
		'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
		'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
		'!', '@', '#', '$', '%', '&', '*', '-', '_', '=','+',
		'1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def newPass():
	if len(sys.argv)>1:
		passwdNum = sys.argv[1]
	else :
		while True:
		    try:
			    passwdNum = int(raw_input("Enter max number of characters: "))
		    except TypeError:
			    print "Please enter a digit."
			    continue
		    break        
	return gen(passwdNum)

def gen(number):
	password = []
	number = int(number)
	count = 0
	while count != number:
		password.append(randomChoice(passData))
		count += 1
	x = 0
	p = ''
	while x != len(password):
		p = p + str(password[x])
		x += 1    
	return p
	
def checkpass(password):
	counter = 0
	pattern_uppercase = '[A-Z]'
	pattern_lowercase = '[a-z]'
	pattern_numbers = '[0-9]'
	pattern_symbols = '[!@#$%&*_=+\-]'
	if re.findall(pattern_uppercase, password):
		counter+=1
	if re.findall(pattern_lowercase, password):
		counter+=1
	if re.findall(pattern_numbers, password):
		counter+=1
	if re.findall(pattern_symbols, password):
		counter+=1
	return(counter)
		
test=0
while test < 4:	
	password= newPass()
	test =  checkpass(password)
print password
	
