from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('blogs/<slug:url>/',views.main,name='blogs') ,
    path('signin/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard')  
    
]

