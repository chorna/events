from django.shortcuts import render

from rest_framework import generics

from ..serializers.book import BookSerializer, BookUpdateSerializer
from ..models import Books


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookUpdateSerializer
    queryset = Books.objects.all()