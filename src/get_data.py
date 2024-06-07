
import requests
from src.db_flask import DBFlask
from src.db_models import Author, Kind
from src.typing_helper import SessionFactory




def get_kinds():
    url = "http://wolnelektury.pl/api/kinds/"
    response = requests.get(url).json()

    return [kind["name"] for kind in response]
def add_kinds(session_factory: SessionFactory):
    kinds = get_kinds()
    with session_factory() as session:
        for kind in kinds:
            if not session.query(Kind).filter_by(name=kind).first():
                kind = Kind(name=kind)
                session.add(kind)
        session.commit()
def get_authors():
    url = "http://wolnelektury.pl/api/authors/"
    response = requests.get(url).json()

    return [author["name"] for author in response]
def add_authors(session_factory: SessionFactory):
    authors = get_authors()
    with session_factory() as session:
        for author in authors:
            if not session.query(Author).filter_by(name=author).first():
                author = Author(name=author)
                session.add(author)
        session.commit()
if __name__ == "__main__":
    db = DBFlask()
    add_kinds(db.db_session_factory)
    add_authors(db.db_session_factory)
