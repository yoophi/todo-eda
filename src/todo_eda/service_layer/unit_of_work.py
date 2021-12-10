import abc

from todo_eda.adaptors.repository import AbstractTodoRepository, MemTodoRepository


class AbstractUnitOfWork(abc.ABC):
    todos: AbstractTodoRepository

    def __init__(
        self,
        todos: AbstractTodoRepository = None,
    ):
        self.todos = todos

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for todo in self.todos.seen:
            while todo.events:
                yield todo.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class MemUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self,
        todos: AbstractTodoRepository = None,
    ):
        super().__init__()
        self.todos = todos

    def __enter__(self):
        self.users = MemTodoRepository()

        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        pass

    def rollback(self):
        pass
