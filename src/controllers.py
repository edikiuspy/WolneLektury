from dataclasses import dataclass

from src.models import Book
from src.repositories import BookRepository

users = []


@dataclass
class CreateBookRequest:
    title: str
    author: str
    kind: str


class BookController:
    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    def create(self, request: CreateBookRequest) -> None:
        repository_req = Book(
            title=request.title, author=request.author, kind=request.kind
        )
        self._repository.create(repository_req)

    def get(self) -> None:
        return self._repository.get()
