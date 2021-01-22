from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('Services/',views.Services,name='Services'),
    path('product/',views.product,name='product'),
    path('Contacts/',views.Contacts,name='Contacts'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
  
]