from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
# Create your views here.
class BookApiView(APIView):
    def get(self, request):
        all_books = Book.objects.all().values()
        return Response({"Message": "List of all books", "Book_list":all_books})

    def post(self, request):
        # Book.objects.all().values
        pass