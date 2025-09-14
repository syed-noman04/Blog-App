from . import views
from django.urls import path

urlpatterns = [
    # path('', views.test),
    path('loginn/', views.loginn),
    path('', views.signup),
    path('home/', views.home),
    path('newpost/', views.newPost),
    path('mypost/', views.myPost),
    path('signout/', views.signOut)
]