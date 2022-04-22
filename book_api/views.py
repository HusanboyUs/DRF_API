from .models import Book
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .serializer import BookSerializer

@api_view(['GET'])
def books_list(request):
    books=Book.objects.all() #Complex Data
    serializer=BookSerializer(books, many=True) #serializer json data
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

api_view(['GET'])
def book(request, pk):
    if request.method =='GET':
        book=Book.objects.get(id=pk)
        serializer=BookSerializer(book)
        return Response(serializer.data)          