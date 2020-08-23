
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

#Get the text from index.html page
   djtext= request.POST.get('text','default')

#Here! POST method is used here to pull all the data through body not through URL
#check checkbox value
   removepunc=request.POST.get('removepunc','off')
   capitalizefont=request.POST.get('capitalizefont','off')
   countcharacter=request.POST.get('countcharacter','off')

   if removepunc == "on":
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed=""
       for char in djtext:
           if char not in punctuations:
               analyzed= analyzed + char
       params= {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
       djtext= analyzed
      # return render(request, 'analyze.html', params)

   if(capitalizefont== "on"):
       analyzed=""
       for char in djtext:
           analyzed= analyzed + char.upper()
       params = {'purpose': 'Making UpperCase', 'analyzed_text': analyzed}
       djtext=analyzed
       #return render(request, 'analyze.html', params)


   if(countcharacter== "on"):
       for char in djtext:
           analyzed= len(djtext)
       params = {'purpose': 'Count a charecter', 'analyzed_text': analyzed}


   if(removepunc != "on"and capitalizefont != "on" and countcharacter != "on"):
       return HttpResponse("Error")

   return render(request, 'analyze.html', params)



