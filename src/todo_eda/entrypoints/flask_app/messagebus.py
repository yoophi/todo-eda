from flask import current_app
from werkzeug.local import LocalProxy

from todo_eda import bootstrap
from todo_eda.adaptors.repository import MemTodoRepository
from todo_eda.service_layer import unit_of_work
from todo_eda.service_layer.messagebus import MessageBus

_bus = None


def get_message_bus():
    global _bus

    if _bus is None:
        todos = MemTodoRepository()
        uow = unit_of_work.MemUnitOfWork(todos=todos)
        print(f"uow={uow}")
        _bus = bootstrap.bootstrap(
            uow=uow,
            logger=current_app.logger,
        )

    return _bus


bus: MessageBus = LocalProxy(get_message_bus)
