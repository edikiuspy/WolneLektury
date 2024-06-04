from dataclasses import dataclass
from typing import Generator

from sqlalchemy.orm import Session

from src.db_models import Author, Kind,Book
from src.db_flask import SessionFactory

books = []


@dataclass
class CreateBookInDBRequest:
    title:str
    author:str
    kind:str


class BookRepository:
    def __init__(self, session_factory: SessionFactory) -> None:
        self._session = next(self.session(session_factory))

    def session(self, session_factory: SessionFactory) -> Generator[Session, None, None]:
        with session_factory() as session:
            yield session

    def create_author(self, author: str) -> Author:
        author=self._session.query(Author).filter_by(name=author).first()
        if not author:
            author = Author(name=author.name)
            self._session.add(author)
            self._session.commit()
        return author

    def create_kind(self, kind: str) -> Kind:
        kind=self._session.query(Kind).filter_by(name=kind).first()
        if not kind:
            kind = Kind(name=kind.name)
            self._session.add(kind)
            self._session.commit()

        return kind




    def create(self, book_params: Book) -> None:
        author = self.create_author(book_params.author)
        kind = self.create_kind(book_params.kind)
        book = Book(title=book_params.title, author_id=author.id, kind_id=kind.id)

        self._session.add(book)
        self._session.commit()

    def get(self):
        result = self._session.query(Book).all()
        print(result)
        print([i.get_dict() for i in result])
        return result
