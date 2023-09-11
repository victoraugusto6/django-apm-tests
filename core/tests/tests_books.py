from core.models import Author, Book
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


def test_get_books(api_client, user):
    author = baker.make(Author)
    book = baker.make(Book)
    book.authors.add(author)

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    response = api_client.get(reverse("core:book-list-create"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["title"] == book.title


def test_get_book(api_client, user):
    author = baker.make(Author)
    book = baker.make(Book)
    book.authors.add(author)

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    response = api_client.get(
        reverse("core:book-retrieve-update-delete", kwargs={"pk": book.pk})
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == book.pk
    assert response.data["title"] == book.title


def test_create_book(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")

    author = baker.make(Author)
    payload = {"title": "book Name", "authors": author.pk}

    response = api_client.post(reverse("core:book-list-create"), data=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.get(title="book Name")


def test_edit_book(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")

    author_1 = baker.make(Author, name="Author 1")
    author_2 = baker.make(Author, name="Author 2")
    book = baker.make(Book, title="Book 1")
    book.authors.add(author_1)

    payload = {"title": "Book 2", "authors": author_2.pk}

    response = api_client.put(
        reverse(
            "core:book-retrieve-update-delete",
            kwargs={"pk": book.pk},
        ),
        data=payload,
    )
    assert response.status_code == status.HTTP_200_OK
    assert Book.objects.get(title="Book 2", authors=author_2.pk)


def test_delete_book(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")

    book = baker.make(Book)

    response = api_client.delete(
        reverse(
            "core:book-retrieve-update-delete",
            kwargs={"pk": book.pk},
        ),
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Book.objects.exists()
