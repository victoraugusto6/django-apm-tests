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


def test_get_authors_using_search(api_client, user):
    author_1 = baker.make(Author, name="Author 1")
    baker.make(Author, name="Author 2")

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    response = api_client.get(
        reverse("core:author-list-create"), data={"search": "Author 1"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    assert response.data["results"][0]["name"] == author_1.name


def test_get_authors_using_ordering(api_client, user):
    baker.make(Author, name="Author 2")
    baker.make(Author, name="Author 3")
    baker.make(Author, name="Author 1")

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {user.auth_token.key}")
    response = api_client.get(
        reverse("core:author-list-create"), data={"ordering": "name"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["name"] == "Author 1"
    assert response.data["results"][1]["name"] == "Author 2"
    assert response.data["results"][2]["name"] == "Author 3"


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
