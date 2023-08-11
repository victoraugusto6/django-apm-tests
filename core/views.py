from django.shortcuts import render

from .models import Book


def home(request):
    books = Book.objects.all().prefetch_related("authors")
    return render(request, "core/home.html", {"books": books})
