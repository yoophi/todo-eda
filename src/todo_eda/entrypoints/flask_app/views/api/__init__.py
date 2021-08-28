from flask import Blueprint, jsonify

from todo_eda.entrypoints.flask_app.schema import TodoSchema

api = Blueprint("api", __name__)


@api.route(
    "/todos",
    methods=[
        "GET",
    ],
)
def todo_list():
    todos = [
        {
            "id": 1,
            "title": "sample",
            "is_completed": True,
        }
    ]
    schema = TodoSchema(many=True)
    return jsonify(schema.dump(todos))


@api.route(
    "/todos",
    methods=[
        "POST",
    ],
)
def todo_create():
    return jsonify({})


@api.route(
    "/todos/<todo_id>",
    methods=[
        "GET",
    ],
)
def todo_detail(todo_id):
    todo = {
        "id": todo_id,
        "title": "sample",
        "is_completed": True,
    }
    schema = TodoSchema()
    return jsonify(schema.dump(todo))


@api.route(
    "/todos/<todo_id>",
    methods=[
        "PUT",
    ],
)
def todo_update(todo_id):
    return jsonify({})


@api.route(
    "/todos/<todo_id>",
    methods=[
        "DELETE",
    ],
)
def todo_remove(todo_id):
    return jsonify({})
