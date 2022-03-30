from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse
from .models import Detail

# Create your views here.

def base(request) :
    return render(request, 'base.html')

def register(request):    
    return render(request, 'register.html')

def login(request) :
    return render(request, 'login.html')

def sidebarbase(request) :
    return render(request, 'sidebarbase.html')

def userhomepage(request) :
    return render(request, 'userhomepage.html')

def hrhomepage(request):
    selected_value = None
    sel_project = None
    # detail = Detail.objects.all()
    project_search = Detail.objects.values_list('project',flat=True).distinct()

    if request.method == 'POST':
        selected_value = request.POST.get('selected_project')
        print(selected_value)
        sel_project = Detail.objects.filter(project__iexact = selected_value)
        print(sel_project)
       
    context = {
        'project_search': project_search,
        'selected_value' : selected_value,
        'sel_project': sel_project,
        }
    return render(request, 'hrhomepage.html' , context)
    
def contentpage(request) :
    return render(request, 'contentpage.html')


