from django.urls import path
from . import views

app_name = "poll"

urlpatterns = [
    path('', views.Homepage, name= "Home"),
    path('Python', views.Pythonpage, name= "python"),
    path('blender', views.blenderpage, name= "blender"),
    
    


]