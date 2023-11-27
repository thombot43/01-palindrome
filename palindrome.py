#!/usr/bin/env python3

def validate(input):
    '''
    Validate user input. Input must be a word.
    '''
    if not word.isalpha():
        print("not a valid input")
    else: 
        return True

def is_palindrome(word):
    '''
    Takes a string and returns True if the string is a palindrome
    '''
    rev = ""
    for i in word:
        rev = i + rev

    if word == rev:
        return(f"'{word}' is a palindrome!!")
    else:
        return(f"'{word}' is NOT a palindrome")


while True:
    print("Enter a word: ")
    word = input().lower()

    if validate(word):
        print(is_palindrome(word))
