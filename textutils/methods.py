from django.shortcuts import render
from django.http import HttpResponse

def removePunctuations(request,userInput):
    punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    analyzed = ""
    for char in userInput:
        if char not in punctuations:
            analyzed = analyzed + char
    userInput = analyzed
    return analyzed
###########################################################################################
def capitalLetters(request,userInput):
    capital= userInput.upper()
    print(HttpResponse("Capital Letters"))
    userInput = capital
    return userInput
###############################################################################################
def lowercaseLetters(request,userInnput):
    lower = userInnput.lower()
    userInnput = lower
    return userInnput
###########################################################
def removeExtraSpaces(request,userInput):
    analyzed = ""
    for index,char in enumerate(userInput):
        if userInput[index] == " " and userInput[index+1] == " ":
            pass
        else:
            analyzed = analyzed + char
    userInput = analyzed
    return userInput
########################################################
def removeNewLine(request,userInput):
    analyzed = ""
    for char in userInput:
        if char != "\n":
            analyzed = analyzed +char
    userInput = analyzed
    return  userInput