from django.urls import path
from . import views

app_name='book_api'

urlpatterns = [
    path('list/', views.BookList.as_view(), name='books-list' ),
    path('', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/', views.BookDetial.as_view(), name='book-detail'),

]


