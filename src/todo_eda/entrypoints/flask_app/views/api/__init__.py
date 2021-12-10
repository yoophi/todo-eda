from flask import Blueprint, jsonify, request

from todo_eda.domain import commands
from todo_eda.entrypoints.flask_app.messagebus import bus
from todo_eda.entrypoints.flask_app.schema import TodoSchema
from todo_eda.views.todos import get_todo_list, get_todo

api = Blueprint("api", __name__)


@api.route(
    "/todos",
    methods=[
        "GET",
    ],
)
def todo_list():
    todos = get_todo_list(bus.uow)
    schema = TodoSchema(many=True)
    return jsonify(schema.dump(todos))


@api.route(
    "/todos",
    methods=[
        "POST",
    ],
)
def todo_create():
    cmd = commands.CreateTodo(title=request.json.get("title"))
    resp = bus.handle(cmd)
    if not resp:
        return jsonify(message=resp.message), 400

    schema = TodoSchema()
    return jsonify(schema.dump(resp.value)), 200


@api.route(
    "/todos/<todo_id>",
    methods=[
        "GET",
    ],
)
def todo_detail(todo_id):
    todo = get_todo(todo_id, bus.uow)
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
