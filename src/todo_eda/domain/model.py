from typing import List, Any


class Todo:
    id: str
    title: str
    completed: bool
    events: List[Any]

    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed
        self.events = []

    def to_dict(self):
        return {
            key: getattr(self, key)
            for key in (
                "id",
                "title",
                "completed",
            )
        }
