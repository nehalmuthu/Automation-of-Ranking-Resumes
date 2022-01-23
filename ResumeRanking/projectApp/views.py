from django.shortcuts import render,redirect 
# get datetime 
import datetime  
from django.http import HttpResponse 
from .models import GeeksModel,JobDescription
from .forms import JDForm
from projectApp.code.code3rank import queryDocs,queryDocs2
from django.core.paginator import Paginator,EmptyPage

# Create your views here. 
def home_view(request): 
    print(request.GET) 
  
    # logic of view will be implemented here 
    return render(request, "home.html") 

# Create your views here. 
def search_view(request): 
    #print(request.GET.get('q'))
    template="searchbox.html"
    query=request.GET.get('q')
    if not query:
        query="z"
    #for search in decscription
    #result=GeeksModel.objects.filter(description__contains=query)
    #for search in title
    result=GeeksModel.objects.filter(title__contains=query)
    
    #print(result)
    context={}
    context["result"]=result
    
    # logic of view will be implemented here 
    return render(request, template,context) 


def search_view_ver2(request): 
    #print(request.GET.get('q'))
    template="search2.html"
    query=request.GET.get('myfile')
    
    print(query)
    return render(request, template) 



def chooseJD(request):
    
    template="radio.html"
    
    if request.method== 'POST':
        query=request.POST.get('title')
        
        #print('query',query)
        #print()
        #if not query:
         #   query="z"
        l=queryDocs(query)
        #print(l)
        #print()
        
        #l=["documentsJD/BAI10010003-Yogin.pdf","devesh"]
        context2 ={} 
        # add the dictionary during initialization 
    
        context2["dataset"] = JobDescription.objects.filter(document__in=l)
        return render(request, template,context2)
        #return render(request, template,context2)
        
    else:
        context ={} 
        context["dataset"] = JobDescription.objects.all()
        return render(request, template,context)
 

def model_form_upload(request):
    if request.method == 'POST':
        form = JDForm(request.POST, request.FILES)
        #print(request.POST)
        if form.is_valid():
            form.save()
        #return redirect(chooseJD)
        return redirect(list_viewjd)
        
    else:
        form = JDForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

# create a function 
def geeks_view(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return response 
    return HttpResponse(html) 


def list_viewjd(request): 
    # dictionary for initial data with  
    # field names as keys 
     
    
    j=JobDescription.objects.all() 
    p=Paginator(j,5)
    
    page_num=request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)
    # add the dictionary during initialization 
    context ={"dataset":page}
                
    return render(request, "list_viewjd.html", context)     

  
def list_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = GeeksModel.objects.all() 
          
    return render(request, "list_view.html", context) 




def chooseJD2(request):
    
    template="docUpSearch.html"
    
    if request.method== 'POST':
        query=request.POST.get('my-file')
        
        print('query',query)
        #print()
        #if not query:
         #   query="z"
        l=queryDocs2(query)
        #print(l)
        #print()
        
        #l=["documentsJD/BAI10010003-Yogin.pdf","devesh"]
        context2 ={} 
        # add the dictionary during initialization 
    
        context2["dataset"] = JobDescription.objects.filter(document__in=l)
        return render(request, template,context2)
        #return render(request, template,context2)
        
    else:
        context ={} 
        context["dataset"] = JobDescription.objects.all()
        j=JobDescription.objects.all() 
        p=Paginator(j,7)
    
        page_num=request.GET.get('page',1)
        try:
            page=p.page(page_num)
        except EmptyPage:
            page=p.page(1)
        # add the dictionary during initialization 
        context ={"dataset":page}
        return render(request, template,context)


  


