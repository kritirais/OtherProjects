# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 23:54:35 2022

@author: CSUFTitan
"""

import sys

print()
print('INFO: This program will try to decipher a monoalphabetic \
substitution cipher.')
print()

try:
    import enchant
    print('INFO: Modules imported successfully.')
except ModuleNotFoundError:
    print('ERROR: Please install pyenchant using the below command and run the \
script again.')
    print('pip install pyenchant')
    sys.exit()

#unigram
unigram = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060, 0.065, \
           0.005, 0.005, 0.035, 0.030, 0.070, 0.080, 0.020, 0.002, \
           0.065, 0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]
    
alphabet = list('abcdefghijklmnopqrstuvwxyz')
english = enchant.Dict("en_US")

cipher = input('Enter the cipher text you want to decipher: ')

sp = cipher.count(' ')  #ignore whitespaces

#getting the frequency of each letter
freqDict = {l : cipher.count(l) / (len(cipher) - sp) for l in cipher \
            if l.strip() != ''}

print()
#examining possible keys by calculating phi
possibleKeys = []
for i in range(26):
    phi = 0
    for c in freqDict:
        if c.strip() != '':
            phi += (freqDict[c] * unigram[alphabet.index(c) - i])
        else:
            continue
    if phi > 0.05:
        possibleKeys.append(chr(i + 97))

#get the plain text
for key in possibleKeys:
    plain = ''
    
    for l in cipher:
        if l.strip() != '':
            plain += alphabet[alphabet.index(l) - alphabet.index(key)]
        else:
            plain += ' '
    
    #check if each word is english in case of multiple words
    check = [word for word in plain.split(' ') if english.check(word)]
    if len(check) == len(plain.split(' ')):
        print("INFO: Plain text: {} and key: '{}'.".format(plain.upper(), key))
        break
else:
    print('ERROR: Could not find the key.')
