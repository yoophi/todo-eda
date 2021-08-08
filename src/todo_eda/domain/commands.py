class Command:
    pass


@dataclass
class CreateTodo(Command):
    title: str
