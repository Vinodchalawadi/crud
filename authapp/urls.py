from django.urls import path, include
from authapp import views
from authapp.views import userAPI, putAPI
urlpatterns = [
    # path('ulist/', views.authuser, name='authuser'),
    # path('home/', views.home, name='home'),
    # path('<int:pk>/',  views.authjson, name='authjson'),
    ##function based views mapping
    path('getuser/', views.getuser, name='getuser'),
    path('auth/<int:pk>/', views.userlist, name='userlist'),
    ##class based views mapping
    path('getapi/', userAPI.as_view(), name='userAPI'),
    path('putAPI/<int:pk>/', putAPI.as_view(), name='putAPI'),
]
