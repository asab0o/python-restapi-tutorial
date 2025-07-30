from flask import Flask, jsonify, request, abort

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item A", "description": "First item"},
    {"id": 2, "name": "Item B", "description": "Second item"},
]

# Simple counter for generating new IDs
next_id = 3

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "404 Not Found"}), 404

@app.route("/items", methods=["GET"])
def get_items():
    """Returns a list of all items."""
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["GET"])
def get_selected_item(item_id):
    """Returns a list of selected item."""
    # Setting None instead of StopIteration error
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

@app.route("/items/search", methods=["GET"])
def search_items():
    """Returns a list of matching item."""
    target_name = request.args.get("name")
    target_description = request.args.get("description")

    filtered_items = items
    if target_name:
        lower_target_name = target_name.lower()
        filtered_items = [item for item in filtered_items if lower_target_name in item["name"].lower()]
    if target_description:
        lower_target_description = target_description.lower()
        filtered_items = [item for item in filtered_items if lower_target_description in item["description"].lower()]

    return jsonify(filtered_items)

@app.route("/items", methods=["POST"])
def add_item():
    global next_id

    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    if "name" not in request.json or "description" not in request.json:
        return jsonify({"error": "Missing 'name' or 'description'"}), 400
    # Exercises 1
    if request.json["name"] == "" or request.json["description"] == "":
        return jsonify({"error": "Bad Request."}), 400
    # Exercises 2 any(): 
    check_duplicate_name = not any(item["name"] == request.json["name"] for item in items)
    if check_duplicate_name:
        return jsonify({"error": "The input data already exists."}), 409
    
    
    new_item = {
        "id": next_id,
        "name": request.json["name"],
        "description": request.json["description"]
    }

    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201

@app.route("/", methods=["GET"])
def hello_world():
    """Returns a simple greeting."""
    return "Hello, World! This is our API."

if __name__ == "__main__":
    app.run(debug=True)
