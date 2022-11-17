import logging

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Book
from book.serialization import BookSerializer


class Books(APIView):
    """
    Class for performing curd operation for book
    """

    def post(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'Message': 'Book Added Successfully', 'data': serializer.data},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response({"message": str(e)}, status=400)

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        book_list = Book.objects.all()
        serializer = BookSerializer(book_list, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        id = pk
        book = Book.objects.get(pk=id)
        serialiser = BookSerializer(book, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response({"Messsage": "Book Updated Successfully"})
        return Response(serialiser.errors)

    def delete(self, request, pk):
        id = pk
        book = Book.objects.get(pk=id)
        book.delete()
        return Response({"Message": "Book Deleted Successfully"})
