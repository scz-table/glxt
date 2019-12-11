from django.urls import path
from . import views
app_name='userextension'
urlpatterns = [
    path('',views.index,name='index'),


]