from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse
from emp.models import Emp

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
    roadhow = Emp.objects.all().filter(project='roadhow')
    avdevs = Emp.objects.all().filter(project='avdevs')
    clara = Emp.objects.all().filter(project='clara')
    streetai = Emp.objects.all().filter(project='streetai')
    ninetofive = Emp.objects.all().filter(project='9tofive')
    
    emp = {'0': roadhow, '1': clara,'2': avdevs, '3':streetai,'4': ninetofive }
    # emp_count = roadhow.count()
    
    context = {
        'emp' : emp,
        # 'emp_count' : emp_count,
    }
    return render(request, 'hrhomepage.html', context)
    
# def Emp_detail(request):
#     emp = Emp.objects.all().filter(project='roadhow')
#     avdevs = Emp.objects.all().filter(project='avdevs')
#     clara = Emp.objects.all().filter(project='clara')
#     streetai = Emp.objects.all().filter(project='streetai')
    
#     # emp = [roadhow, avtracker, clara, streetai ]
#     # emp_count = emp.count()
    
#     context = {
#         'emp' : emp,
#         'emp_count' : emp_count,
#     }
#     return render(request, 'hrhomepage.html' , context)
    
def contentpage(request) :
    return render(request, 'contentpage.html')


