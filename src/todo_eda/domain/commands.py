import abc
from dataclasses import dataclass


class Command(abc.ABC):
    @abc.abstractmethod
    def is_valid(self):
        raise NotImplementedError


@dataclass
class CreateTodo(Command):
    title: str

    def is_valid(self):
        return True


@dataclass
class UpdateTodo(Command):
    id: int
    title: str
    is_completed: bool

    def is_valid(self):
        return True


@dataclass
class RemoveTodo(Command):
    id: int

    def is_valid(self):
        return self.id > 0
