from typing import Generator

from sqlalchemy.orm import Session, joinedload

from src.db_models import Author, Kind,Book
from src.db_flask import SessionFactory

class BookRepository:
    def __init__(self, session_factory: SessionFactory) -> None:
        self._session = next(self.session(session_factory))

    def session(self, session_factory: SessionFactory) -> Generator[Session, None, None]:
        with session_factory() as session:
            yield session

    def create_author(self, author: str) -> Author:
        author_q=self._session.query(Author).filter_by(name=author).first()
        if not author_q:
            author_q = Author(name=author)
            self._session.add(author_q)
            self._session.commit()
        return author_q

    def create_kind(self, kind: str) -> Kind:
        kind_q=self._session.query(Kind).filter_by(name=kind).first()
        if not kind_q:
            kind_q = Kind(name=kind)
            self._session.add(kind_q)
            self._session.commit()

        return kind_q




    def create(self, book_params: Book) -> None:
        author = self.create_author(book_params.author)
        kind = self.create_kind(book_params.kind)
        book = Book(title=book_params.title, author_id=author.id, kind_id=kind.id)

        self._session.add(book)
        self._session.commit()

    def get(self, title=None) -> list[dict]:
        if title:
            result = self._session.query(Book).options(joinedload(Book.author), joinedload(Book.kind)).filter(
                Book.title == title).all()
        else:
            result = self._session.query(Book).options(joinedload(Book.author), joinedload(Book.kind)).all()
        return [i.get_dict() for i in result]

    def search(self,search_params) -> list[dict]:
        query = self._session.query(Book)
        if search_params.author:
            query = query.join(Author).filter(Author.name == search_params.author)
        if search_params.kind:
            query = query.join(Kind).filter(Kind.name == search_params.kind)
        result = query.all()
        return [i.get_dict() for i in result]