from flask import Flask
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

from src.db_models import Base
from src.typing_helper import SessionFactory


class DBFlask(Flask):
    def run(self, *args, **kwargs) -> None:
        Base.metadata.create_all(bind=self.db_engine)
        super().run(*args, **kwargs)

    @property
    def db_session_factory(self) -> SessionFactory:
        return sessionmaker(bind=self.db_engine)

    @property
    def db_engine(self) -> Engine:
        return create_engine('postgresql://docker:docker@localhost:5432/wolnelektury_db')
