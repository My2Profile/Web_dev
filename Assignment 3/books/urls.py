from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.book_list, name='book_list'),

    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    
    path('genres/add/', views.add_genre, name='add_genre'),

]