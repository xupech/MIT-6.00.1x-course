#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 13:57:28 2019

@author: xupech
"""

from ps3_hangman import *
import string

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        while letter not in lettersGuessed:
            return False
    return True
""" Did the user get all letters, i.e., the word? """

def getGuessedWord(secretWord, lettersGuessed):
    new_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            new_word += letter
        else:
            new_word+='_ '
    return new_word

"""show the guessed letters"""

def getAvailableLetters(lettersGuessed):
    All_letters = string.ascii_lowercase
    new_all= ''
    for letter in All_letters:
        if letter not in lettersGuessed:
            new_all += letter
    return new_all

def hangman(secretWord):
    lettersGuessed = []
    i = 8
    
    while i != 1 and isWordGuessed(secretWord, lettersGuessed) == False:
        print ('-------------')
        print ('You have '+ str(i)+' guesses left.')
        print ('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        letter_input = input ('Please guess a letter: ')
        letter_input = letter_input.lower()
        
        if letter_input in secretWord:
            if letter_input in lettersGuessed:
                print ('Oops, you have already taken that guess.')
            else:
                lettersGuessed+= letter_input
                print ('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            
        
        else:
            if letter_input in lettersGuessed:
                print ('Oops, you have already taken that guess.')  
            else:
                lettersGuessed+= letter_input
                print ('Oops! That letter is not in my word ' + str(getGuessedWord(secretWord, lettersGuessed)))
            i-=1
    

    if isWordGuessed(secretWord, lettersGuessed) == True:
        print ('-------------')
        return print('Congratulations, you won')
        
    elif i == 1:
        print ('-------------')
        return print ('Sorry, you ran out of guesses. The word was ' + secretWord +'.')
    
        
            
                