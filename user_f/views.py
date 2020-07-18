from django.shortcuts import render,HttpResponse,redirect



def home(request):
    return render(request,'home.html');


def analyze(request):
    #get the text
    djtext =request.POST.get('text','default ')

    #Cheak the cheakbox value
    removepunc =request.POST.get('removepunc','off')
    uppercase =request.POST.get('uppercase','off')
    newlineremover =request.POST.get('newlineremover','off')
    extraspaceremover =request.POST.get('extraspaceremover','off')
    caractercount =request.POST.get('caractercount','off')
    
    
    # print(removepunc)
    # print(djtext)

    #cheak cheakbox on and perform opration
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        #analyzed = djtext
        params = {'purpose':'Remove punctuation','analyzed_text': analyzed}
        djtext = analyzed
    
        #analyze the text
        # return render(request,"analyze.html", params)

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        #uppercase
        params = {'purpose':'Capitalize','analyzed_text': analyzed}
        djtext = analyzed

        #analyze the text
        # return render(request,"analyze.html", params)
    
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        #uppercase
        params = {'purpose':'NEW LINE REMOVER','analyzed_text': analyzed}
        djtext = analyzed

        #analyze the text
        # return render(request,"analyze.html", params)
    
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):

            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        #uppercase
        params = {'purpose':'Remove Extra Space','analyzed_text': analyzed}
        djtext = analyzed

        #analyze the text
        # return render(request,"analyze.html", params)

    if caractercount == "on":
        analyzed = 0
        for index, char in enumerate(djtext):

            if not(djtext[index] == " "):
                analyzed = analyzed + 1
        analyzed = djtext + " = " + str(analyzed) 
        #uppercase
        params = {'purpose':'Remove Extra Space','analyzed_text': analyzed}

    if (removepunc != "on" and uppercase != "on" and newlineremover != "on" and extraspaceremover != "on" and caractercount != "on" ):
        params = {'error':'error(497)','errordis': 'please select any one option'}
        return render(request,"error.html", params)
        
        
        #analyze the text
    return render(request,"analyze.html", params)
    


    


            


    

    


# Create your views here.
