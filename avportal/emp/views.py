from django.shortcuts import render
from .models import Emp

# Create your views here.

def Emp_detail(request):
    emp = Emp.objects.all().filter(project='streetai')
    emp_count = emp.count()
    
    context = {
        'emp' : emp,
        'emp_count' : emp_count,
    }
    return render(request, 'emp.html' , context)