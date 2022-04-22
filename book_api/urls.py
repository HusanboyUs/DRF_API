from django.urls import path
from . import views

app_name='book_api'

urlpatterns = [
    path('list/', views.books_list, name='books-list' ),
    path('', views.book_create, name='book-create' ),
    path('books/<int:pk>/', views.book, name='book' ),
]
