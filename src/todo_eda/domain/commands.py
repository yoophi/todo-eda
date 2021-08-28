from dataclasses import dataclass


class Command:
    pass


@dataclass
class CreateTodo(Command):
    title: str


@dataclass
class UpdateTodo(Command):
    id: int
    title: str
    is_completed: bool


@dataclass
class RemoveTodo(Command):
    id: int
