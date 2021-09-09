from django.urls import path
from main import views

urlpatterns = [
    path ('pc', views.profile_create, name = 'pc/' ),
    path('profile', views.profile_read, name = 'read/' ),
    #path('<str:uname>', views.libum, name = 'linkers/' ),
    #path('<int:pk>/feedback', views.fed, name = 'feed/' ),
]