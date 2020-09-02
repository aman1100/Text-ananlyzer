#I have created this file - Aman
from django.http import HttpResponse
from django.shortcuts import render
from . import methods

def index (request):
    return render(request, 'index.html')
def analyzer (request):
    userInput = request.POST.get('text', 'default')
    removePunc = request.POST.get('removePunc' , 'off')
    capitalLetters = request.POST.get('capitalLetters', 'off')
    lowercaseLetters = request.POST.get('lowercaseLetters', 'off')
    removeExtraspaces = request.POST.get('removeExtraspaces' ,'off')
    removeNewLine = request.POST.get('removeNewLine','off')

    if(removePunc == 'on'):
      userInput=  methods.removePunctuations(request,userInput)
    if(capitalLetters == 'on'):
        userInput = methods.capitalLetters(request, userInput)
    if(lowercaseLetters == 'on'):
        userInput= methods.lowercaseLetters(request,userInput)
    if(removeExtraspaces == 'on'):
        userInput= methods.removeExtraSpaces(request,userInput)
    if(removeNewLine == 'on'):
        userInput= methods.removeNewLine(request,userInput)
    if(removePunc!='on' and capitalLetters!='on' and lowercaseLetters!='on' and removeExtraspaces!='on' and removeNewLine != 'on'):
        return HttpResponse('Error Please select any Checkbox!!!!')
    props = {'analyzed_text' : userInput}
    return render(request,'analyzed.html',props)
