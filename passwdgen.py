#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Generate a password that is good enough for WUR use

Usage : passwdgen.py [length of password]

"""
import sys
from random import choice as randomChoice
import re

characters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '!',
    '@',
    '#',
    '$',
    '%',
    '&',
    '*',
    '-',
    '_',
    '=',
    '+',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    ]


def newPass():
    """Get the length of the password, and generate it """
    if len(sys.argv) > 1:
        password_length = sys.argv[1]
    else:
        while True:
            try:
                password_length = \
                    int(raw_input('Enter maximum number of characters: '))
            except (TypeError, ValueError):
                print 'Please enter a digit.'
                continue
            break
    return generate(password_length)


def generate(number):
    """Generate a random password, with the characters from characterlist """
    password = []
    number = int(number)
    count = 0
    while count != number:
        password.append(randomChoice(characters))
        count += 1
    #Turn password list into string and return
    return ''.join(password)


def checkpass(password):
    """Check for adherence to the password rules, and return number of hits """
    hitcounter = 0
    pattern_uppercase = '[A-Z]'
    pattern_lowercase = '[a-z]'
    pattern_numbers = '[0-9]'
    pattern_symbols = '[!@#$%&*_=+\-]'
    if re.findall(pattern_uppercase, password):
        hitcounter += 1
    if re.findall(pattern_lowercase, password):
        hitcounter += 1
    if re.findall(pattern_numbers, password):
        hitcounter += 1
    if re.findall(pattern_symbols, password):
        hitcounter += 1
    return hitcounter


if len(sys.argv) > 2:
    numberOfPasswords = int(sys.argv[2])
else:
    numberOfPasswords = 1

for counter in range(0, numberOfPasswords):
    test = 0
    while test < 4:
        password = newPass()
        test = checkpass(password)
    print password
