from django.contrib.auth.models import User

from rest_framework import viewsets, generics

from api.serializers import UserSerializer, BookSerializer, PublisherSerializer, AuthorSerializer, RatingSerializer, \
    AuthorBooksSerializer
from pinkflamingo.models import Book, Publisher, Author, Rating


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class AuthorBooks(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorBooksSerializer