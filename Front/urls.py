from django.urls import path
from . import views
app_name='front'
urlpatterns = [
    path('',views.index,name='front_index'),
    path('console/',views.console,name='front_console'),
    path('signin/',views.signin,name='front_signin'),
    path('signup/',views.signup,name='front_signup'),
    path('my_logout/',views.my_logout,name='my_logout'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('change-password/',views.change_password,name='change_password'),
    path('user-Show-Information/',views.user_Show_Information,name='user_Show_Information'),
    path('user-Edit-Information/',views.user_Edit_Information,name='user_Edit_Information'),
    path('test/',views.test,name='test'),
    path('my-image/',views.my_image,name='my_image'),


]