from dataclasses import dataclass

from todo_eda.domain.model import Todo


class Event:
    pass


@dataclass
class TodoCreated(Event):
    todo: Todo
