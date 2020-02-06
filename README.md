# todoapp_backend
Simple backend API for a todo app using:

* Flask
* Flask-RESTful
* Marshmallow
* Blueprint
* Mongoengine

## To test the app in your machine:

```
git clone https://github.com/Mustapha90/todoapp_backend.git
cd todoapp_backend
python run.py
```

You can also check it out at heroku:
[https://todoapp-backend-mus.herokuapp.com/api/todoitem](https://todoapp-backend-mus.herokuapp.com/api/todoitem
)

## Supported operations:
Endpoint: https://todoapp-backend-mus.herokuapp.com/api/todoitem 

### Get list of all todo items in database:
method: POST  
body: Not required


### Create todo item example:
method: POST  
body: {"title": "Todo item title"}

### Update todo item example:
method: PUT  
body: {"id": "4547455644", isCompleted: true, title: "New title"}

### Delete todo item example:
method: DELETE  
body: {"id": "4547455644"}






