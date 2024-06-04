from src.controllers import BookController
from src.db_flask import DBFlask
from src.repositories import BookRepository
from src.views import BookView

app = DBFlask(__name__)


app.add_url_rule(
    "/books",
    "create_book",
    view_func=BookView.as_view(
        "create_book",
        controller=BookController(
            repository=BookRepository(app.db_session_factory)
        ),
    )
)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
