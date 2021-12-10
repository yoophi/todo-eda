import logging
from typing import Type, Dict, Callable, List, Union

from todo_eda.domain import commands, events
from todo_eda.service_layer import unit_of_work

logger = logging.getLogger(__name__)

Message = Union[commands.Command, events.Event]


class MessageBus:
    def __init__(
        self,
        uow: unit_of_work.AbstractUnitOfWork,
        event_handlers: Dict[Type[events.Event], List[Callable]],
        command_handlers: Dict[Type[commands.Command], Callable],
    ):
        self.uow = uow
        self.event_handlers = event_handlers
        self.command_handlers = command_handlers
        self.queue = []

    def handle(self, message: Message):
        self.queue = [message]
        response = None

        while self.queue:
            message = self.queue.pop(0)
            logger.info(f"MESSAGE: {message}")
            if isinstance(message, events.Event):
                self.handle_event(message)
            elif isinstance(message, commands.Command):
                response = self.handle_command(message)
            else:
                raise Exception(f"{message} was not an Event of Command")

        return response

    def handle_event(self, event: events.Event):
        for handler in self.event_handlers[type(event)]:
            try:
                logger.debug("handling event %s with handler %s", event, handler)
                handler(event)
                self.queue.extend(self.uow.collect_new_events())
            except Exception:
                logger.exception("Exception handling event %s", event)
                continue

    def handle_command(self, command):
        logger.debug("handling command %s", command)
        response = None
        try:
            handler = self.command_handlers[type(command)]
            response = handler(command)
            self.queue.extend(self.uow.collect_new_events())
        except Exception:
            logger.exception("Exception handling command %s", command)
            raise

        return response
