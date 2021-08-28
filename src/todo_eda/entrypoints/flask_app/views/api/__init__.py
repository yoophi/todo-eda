from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/todos', methods=['GET', ])
def todo_list():
    return jsonify({})


@api.route('/todos', methods=['POST', ])
def todo_create():
    return jsonify({})


@api.route('/todos/<int:id>', methods=['GET', ])
def todo_detail(id):
    return jsonify({})


@api.route('/todos/<int:id>', methods=['PUT', ])
def todo_update(id):
    return jsonify({})


@api.route('/todos/<int:id>', methods=['DELETE', ])
def todo_remove(id):
    return jsonify({})
