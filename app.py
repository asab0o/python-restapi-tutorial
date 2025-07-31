from flask import Flask, jsonify, request, abort

app = Flask(__name__)

class Todo:
    def __init__ (self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    
    def __repr__(self):
        return print(f"Todo(id={self.id}, title={self.title})")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    def update_from_dict(self, data):
        if "title" in data: self.title = data["title"]
        if "description" in data: self.description = data["description"]
        if "completed" in data: self.completed = data["completed"]

class TodoManager:
    def __init__(self):
        self.todos = []
        self.next_id = 1
        # dummy data
        self.add_todo("Learn Flask", "Understand the basics of Flask framework.")
        self.add_todo("Build API", "Create a RESTful API for a ToDo list.")

    def add_todo(self, title, description, completed=False):
        if not title or not description:
            raise ValueError
        todo = Todo(self.next_id, title, description, completed)
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def get_all_todos(self):
        return [todo.to_dict() for todo in self.todos]
    
    def get_todo_by_id(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
            else:
                return None
    
    def update_todo(self, todo_id, new_data):
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            return None
        if not new_data:
            return None
        todo.update_from_dict(new_data)
        return todo.to_dict()
    
    def delete_todo(self, todo_id):
        original_len = len(self.todos)
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        return len(self.todos) < original_len

todo_manager = TodoManager()

# --- API Sections ---

@app.route("/todos", methods=["GET"])
def get_todos():
    """Returns a list of all todos."""
    return jsonify(todo_manager.get_all_todos())

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    """Returns a list of all todos."""
    todo = todo_manager.get_todo_by_id(todo_id)
    if todo is None:
        abort(404)
    return jsonify(todo.to_dict())

@app.route("/todos", methods=["POST"])
def create_todo():
    if not request.json:
        abort(400)
    if "title" not in request.json or "description" not in request.json:
        abort(400)
    
    new_title = request.json["title"]
    new_description = request.json["description"]
    new_completed = request.json.get("completed", False)
    try:
        new_todo = todo_manager.add_todo(new_title, new_description, new_completed)
    except ValueError:
        abort(400, description="Failed to create todo. Title or description might be empty.")

    return jsonify(new_todo.to_dict()), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if not request.json:
        abort(400)
    
    update_todo = todo_manager.update_todo(todo_id, request.json)
    if update_todo is None:
        abort(404)

    return jsonify(update_todo), 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if not todo_manager.delete_todo(todo_id):
        abort(404, description="Failed to delete todo.")
    return jsonify({"message": "Todo deleted successfully"}), 204

# Custom error handler for 404 Not Found errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": error.description or "The requested resource was not found."}), 404

# Custom error handler for 400 Bad Request errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": error.description or "The request was malformed or missing required parameters."}), 400

@app.route("/", methods=["GET"])
def hello_world():
    """Returns a simple greeting."""
    return "Hello, World! This is our API."

if __name__ == "__main__":
    app.run(debug=True)
