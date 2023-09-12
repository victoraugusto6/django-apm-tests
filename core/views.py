from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ["name"]
    ordering_fields = ["name", "id"]

    @method_decorator(cache_page(settings.CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AuthorSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ["title", "authors__name"]
    ordering_fields = ["title"]

    def get_queryset(self):
        return Book.objects.all().prefetch_related("authors")


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all().prefetch_related("authors")
