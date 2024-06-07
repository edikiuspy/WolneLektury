from flask import Flask

from src.controllers import BookController
from src.db_flask import DBFlask
from src.repositories import BookRepository
from src.views import BookView, SearchView

app=Flask(__name__)

db=DBFlask()
app.add_url_rule(
    "/books",
    "books",
    view_func=BookView.as_view(
        "books",
        controller=BookController(
            repository=BookRepository(db.db_session_factory)
        ),
    )
)
app.add_url_rule(
    "/book/<string:title>",
    "book",
    view_func=BookView.as_view(
        "book",
        controller=BookController(
            repository=BookRepository(db.db_session_factory)
        ),
    )
)
app.add_url_rule(
    "/search",
    "search_book",
    view_func=SearchView.as_view(
        "search_book",
        controller=BookController(
            repository=BookRepository(db.db_session_factory)
        ),
    )
)


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
