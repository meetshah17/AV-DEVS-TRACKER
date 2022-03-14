from django.contrib import admin
from .models import Emp
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'email', 'project')
    
admin.site.register(Emp, EmpAdmin)