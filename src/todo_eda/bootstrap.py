import inspect
import logging

from todo_eda.service_layer import unit_of_work, handlers, messagebus


def bootstrap(
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work.MemUnitOfWork(),
    logger: logging.Logger = None,
):
    dependencies = {
        "uow": uow,
        "logger": logger,
    }
    injected_event_handlers = {
        event_type: [
            inject_dependencies(event_handler, dependencies)
            for event_handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(command_handler, dependencies)
        for command_type, command_handler in handlers.COMMAND_HANDLERS.items()
    }
    bus = messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )

    return bus


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)
