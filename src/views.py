from flask import Response, request
from flask.views import MethodView

from src.controllers import BookController, CreateBookRequest


class BookView(MethodView):
    def __init__(self, controller: BookController) -> None:
        self._controller = controller

    def post(self) -> Response:
        body = request.json
        if any(key not in body for key in ("title", "author", "kind")):
            return Response(status=400)
        controller_req = CreateBookRequest(
            title=body["title"],
            author=body["author"],
            kind=body["kind"],
        )
        try:
            self._controller.create(controller_req)
        except NotImplementedError:
            pass
        return Response(status=201)
    def get(self) -> Response:
        try:
            self._controller.get()
        except NotImplementedError:
            pass
        return Response(status=201)
