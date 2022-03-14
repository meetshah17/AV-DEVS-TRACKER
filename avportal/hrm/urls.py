from django.contrib import admin
from django.urls import path
from hrm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base, name='home'),
    path('register', views.register , name='register'),
    path('login', views.login , name='login'),
    path('sidebarbase', views.sidebarbase, name='sidebarbase'),
    path('hrhomepage', views.hrhomepage, name='hrhomepage'),
    path('userhomepage', views.userhomepage, name='userhomepage'),
    path('contentpage', views.contentpage, name='contentpage'),
    # path('hrhomepage', views.Emp_detail, name='empdetail'),

]