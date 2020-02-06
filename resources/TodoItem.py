from flask import request
from flask_restful import Resource
from models import TodoItem, TodoItemSchema

todo_items_schema = TodoItemSchema(many=True)
todo_item_schema = TodoItemSchema()


class TodoItemResource(Resource):
    def get(self):
        todo_items = TodoItem.objects.all()
        todo_items = todo_items_schema.dump(todo_items).data
        return {'status': 'success', 'data': todo_items}, 200

    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No valid data provided'}, 400

        # Deserialize input
        data, errors = todo_item_schema.load(json_data)
        if errors:
            return errors, 422

        todo_item = TodoItem.objects(title=data['title']).first()
        if todo_item:
            return {'message': 'A todo item with the same title already exists'}, 400

        todo_item = TodoItem(title=json_data['title'])
        todo_item.save()

        # Serialize and dump input
        result = todo_item_schema.dump(todo_item).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No valid data provided'}, 400

        print(json_data)
        data, errors = todo_item_schema.load(json_data)

        if errors:
            return errors, 422

        todo_item = TodoItem.objects(id=data['id']).first()

        if not todo_item:
            return {'message': 'Todo item does not exist'}, 400

        todo_item.update(**json_data)
        todo_item.save()

        result = todo_item_schema.dump(todo_item).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)

        if not json_data['id']:
            return {'message': 'No id was provided'}, 400

        TodoItem.objects(id=json_data['id']).delete()

        return {"status": 'success'}, 204


