import abc
import uuid

from todo_eda.domain.model import Todo


class AbstractTodoRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    def get(self, todo_id):
        return self._get(todo_id)

    def get_list(
        self,
    ):
        return self._get_list()

    def add(self, title):
        return self._add(title)

    @abc.abstractmethod
    def _add(self, title):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, todo_id):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_list(
        self,
    ):
        raise NotImplementedError


class MemTodoRepository(AbstractTodoRepository):
    def __init__(self):
        super().__init__()
        self._todos = set()

    def _get(self, todo_id):
        try:
            return next(todo for todo in self._todos if todo.id == todo_id)
        except StopIteration:
            return None

    def _get_list(
        self,
    ):
        return (todo for todo in self._todos)

    def _add(self, title):
        todo_id = str(uuid.uuid4())
        todo = Todo(id=todo_id, title=title, completed=False)
        self._todos.add(todo)

        return todo
