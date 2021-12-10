import logging

from todo_eda.domain import commands, events
from todo_eda.response_objects import ResponseFailure, ResponseSuccess
from todo_eda.service_layer import unit_of_work


def handle_create_todo(
    command: commands.CreateTodo,
    uow: unit_of_work.AbstractUnitOfWork = None,
    logger: logging.Logger = None,
):
    if not command.is_valid():
        return ResponseFailure.build_from_invalid_command(command)

    with uow:
        todo = uow.todos.add(command.title)
        todo.events.append(events.TodoCreated(todo=todo))
        uow.todos.seen.add(todo)

    return ResponseSuccess(todo)


def handle_update_todo(
    command: commands.UpdateTodo,
    logger: logging.Logger = None,
):
    if not command.is_valid():
        return ResponseFailure.build_from_invalid_command(command)

    return ResponseSuccess([])


def handle_remove_todo(
    command: commands.RemoveTodo,
    logger: logging.Logger = None,
):
    if not command.is_valid():
        return ResponseFailure.build_from_invalid_command(command)

    return ResponseSuccess(True)


def handle_todo_craeted(
    event: events.Todo,
    logger: logging.Logger = None,
):
    logger.info("Todo created")


EVENT_HANDLERS = {
    events.TodoCreated: [
        handle_todo_craeted,
    ],
}

COMMAND_HANDLERS = {
    commands.CreateTodo: handle_create_todo,
    commands.UpdateTodo: handle_update_todo,
    commands.RemoveTodo: handle_remove_todo,
}
