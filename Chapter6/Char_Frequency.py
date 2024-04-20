# -*- coding: utf-8 -*-
def replaceSymbols(string):
    for char in string:
        if char in "~!@#$%^&()[]{},+-*|/?<>'.;:\"":
            string = string.replace(char, ' ')
    return string

def counts(string):
    wordlist = string.split()
    for word in wordlist:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1

song = "I have a pen. I have an apple, Apple pen. I have a pen. I have pineapple. \
    pineapple pen, Apple pen, Pineapple pen, Pen pineapple, apple pen."

result = {}

tmp = replaceSymbols(song.lower())

counts(tmp)
print(result)