from core.views import (
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)
from django.urls import path

app_name = "core"

urlpatterns = [
    path("authors/", AuthorListCreateAPIView.as_view(), name="author-list-create"),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyAPIView.as_view(),
        name="author-retrieve-update-delete",
    ),
    path("books/", BookListCreateAPIView.as_view(), name="book-list-create"),
    path(
        "books/<int:pk>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-retrieve-update-delete",
    ),
]
