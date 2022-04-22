from asyncore import read
from turtle import title
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=15)
    number_of_pages=serializers.IntegerField()
    publish_date=serializers.DateField()
    quantity=serializers.IntegerField()

    def create(self,data):
        return Book.objects.create(**data)