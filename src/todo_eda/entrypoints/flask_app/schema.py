from .extensions import ma


class TodoSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "is_completed", "_links")

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("api.todo_detail", values=dict(todo_id="<id>")),
            "collection": ma.URLFor("api.todo_list"),
        }
    )
