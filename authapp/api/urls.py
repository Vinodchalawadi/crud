from django.urls import path
from authapp.api.views import userlist, getuser 
 

urlpatterns = [
    path('ulist/', getuser, name='getuser'),
    # path('home/', home, name='home'),
    path('<int:pk>',  userlist, name='userlist'),
]
