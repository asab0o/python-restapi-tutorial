from flask import Flask, jsonify, request, abort

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item A", "description": "First item"},
    {"id": 2, "name": "Item B", "description": "Second item"},
    {"id": 3, "name": "Item C", "description": "Third item"},
]

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

@app.route("/", methods=["GET"])
def hello_world():
    """Returns a simple greeting."""
    return "Hello, World! This is our API."

if __name__ == "__main__":
    app.run(debug=True)
