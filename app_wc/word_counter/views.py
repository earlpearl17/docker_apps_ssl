from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse('Hello')
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increment
            worddictionary[word] += 1
        else:
            #Add to worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    #return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary})
    return render(request, 'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
