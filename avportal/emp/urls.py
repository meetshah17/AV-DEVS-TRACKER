from django.urls import path
from . import views

urlpatterns = [
    path('',views.Emp_detail, name='Emp_detail')
] 