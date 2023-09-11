from core.models import Author
from django.urls import reverse
from model_bakery import baker
from rest_framework import status


def test_get_authors(api_client, user):
    author = baker.make(Author)

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    response = api_client.get(reverse("core:author-list-create"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["name"] == author.name


def test_get_author(api_client, user):
    author = baker.make(Author)

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    response = api_client.get(
        reverse("core:author-retrieve-update-delete", kwargs={"pk": author.pk})
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == author.pk
    assert response.data["name"] == author.name


def test_create_author(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")

    payload = {"name": "Author Name"}

    response = api_client.post(reverse("core:author-list-create"), data=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Author.objects.get(name="Author Name")


def test_edit_author(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")

    author = baker.make(Author, name="Author Name")
    payload = {"name": "Author Name 2"}

    response = api_client.put(
        reverse(
            "core:author-retrieve-update-delete",
            kwargs={"pk": author.pk},
        ),
        data=payload,
    )
    assert response.status_code == status.HTTP_200_OK
    assert Author.objects.get(name="Author Name 2")


def test_delete_author(api_client, user):
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")

    author = baker.make(Author)

    response = api_client.delete(
        reverse(
            "core:author-retrieve-update-delete",
            kwargs={"pk": author.pk},
        ),
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Author.objects.exists()
