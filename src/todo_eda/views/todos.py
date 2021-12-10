from todo_eda.service_layer import unit_of_work


def get_todo(todo_id, uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        return uow.todos.get(todo_id)


def get_todo_list(uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        return uow.todos.get_list()
