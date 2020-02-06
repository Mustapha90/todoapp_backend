from flask_marshmallow import Marshmallow
import mongoengine
import datetime
from bson import ObjectId
from marshmallow import Schema, fields

# Initialize marshmallow
ma = Marshmallow()

# Initialize monoengine db connector
db = mongoengine

db.connect(host='mongodb+srv://mongodbuser:jjwQZ0J0j9P2j6aL@cluster0-3u8nd.mongodb.net/test?retryWrites=true&w=majority')

# Map ObjectId field type to string
Schema.TYPE_MAPPING[ObjectId] = fields.String


# TodoItem document
class TodoItem(db.Document):
    title = db.StringField(max_length=64, required=True)
    description = db.StringField(max_length=128, default="")
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    deadline = db.DateTimeField(default=None)
    isCompleted = db.BooleanField(default=False)

    def __repr__(self):
        return '<TodoItem with title: ' % self.title % '>'


# TodoItem schema
class TodoItemSchema(ma.Schema):
    id = fields.String()
    title = fields.String(required=True)
    description = fields.String(dump_only=True)
    deadline = fields.String(dump_only=True)
    created_at = fields.String(dump_only=True)
    isCompleted = fields.Boolean(default=False)


