from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def analyze(request):
    if request.method=='GET':
        # Get the text
        djtext=request.GET.get("text",'default')

        # check checkbox values
        removepunc = request.GET.get("removepunc",'off')
        fullcaps = request.GET.get("fullcapitalize",'off')
        newlineremover = request.GET.get("newlineremover",'off')
        extraspaceremover = request.GET.get("extraspaceremover",'off')
        charcounter = request.GET.get("charcounter",'off')
        
        # check which checkbox is on
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed=""
            for char in djtext:
               if char not in punctuations:
                 print(char)
                 analyzed= analyzed + char    
            param={'purpose':'Removed Punctuations',
                   'analyzed':analyzed}
            djtext=analyzed
            
            # return render(request,'analyze.html',param)
        if(fullcaps=="on"):
            analyzed=""
            for char in djtext:
                  analyzed=analyzed + char.upper()
            param={'purpose':'Changed To Uppercase',
                   'analyzed':analyzed}
            djtext=analyzed
            # return render(request,'analyze.html',param)
        if(extraspaceremover=="on"):
            analyzed=""
            for index,char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index+1]==' '):
                  analyzed=analyzed + char
            param={'purpose':'Extra Space Remover',
                   'analyzed':analyzed}
            djtext=analyzed
            # return render(request,'analyze.html',param)
        if(newlineremover=="on"):
            analyzed=""
            for char in djtext:
                if char != "\n" and char!="\r":
                  analyzed=analyzed + char
                else:
                    print("no")
            print("pre",analyzed)
            param={'purpose':'New Line Remover',
                   'analyzed':analyzed}
            djtext=analyzed
            # return render(request,'analyze.html',param)
        
        # if(charcounter=="on"):
        #     analyzed=""
        #     count=0
        #     for char in djtext:
        #           analyzed =count=count+1
                  
        #     param={'purpose':'Total words count',
        #            'analyzed':analyzed}
        
        
        if(removepunc!="on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover!="on"):
            return HttpResponse("Please select any operations")
        return render(request,'analyze.html',param)
        # else:
        #     
        
