from dataclasses import dataclass

from src.models import Book
from src.repositories import BookRepository

users = []


@dataclass
class CreateBookRequest:
    title: str
    author: str
    kind: str
@dataclass
class SearchBookRequest:
    author: str | None = None
    kind: str | None = None

class BookController:
    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    def create(self, request: CreateBookRequest) -> None:
        repository_req = Book(
            title=request.title, author=request.author, kind=request.kind
        )
        self._repository.create(repository_req)

    def get(self,title=None) -> list[dict]:
        return self._repository.get(title=title)

    def search(self, author: str = None, kind: str = None) -> list[dict]:
        search_params = SearchBookRequest(author=author, kind=kind)
        return self._repository.search(search_params)
