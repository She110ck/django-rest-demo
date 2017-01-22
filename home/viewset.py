from home.serialize import AuthorSerializer, BookSerializer, BookAdvancedSerializer

__author__ = 'kadgar'
from rest_framework import routers, viewsets
from .models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAdvancedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookAdvancedSerializer


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'books-adv', BookAdvancedViewSet)
