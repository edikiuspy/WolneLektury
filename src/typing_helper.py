from typing import Callable

from sqlalchemy.orm import Session


SessionFactory = Callable[[], Session]
