from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
   
    path('contact.html',views.contact,name="contact")
]
