from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Kind(Base):
    __tablename__ = 'kinds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    kind_id = Column(Integer, ForeignKey('kinds.id'), nullable=False)

    author = relationship('Author', backref='books')
    kind = relationship('Kind', backref='books')

    def get_dict(self) -> dict:
        book_dict = self.__dict__
        book_dict.pop('_sa_instance_state')
        return book_dict