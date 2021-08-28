class Todo:
    id: str
    title: str
    completed: bool

    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            key: getattr(self, key)
            for key in (
                "id",
                "title",
                "completed",
            )
        }
