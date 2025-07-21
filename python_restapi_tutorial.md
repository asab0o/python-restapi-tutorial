# Python REST API Tutorial with Flask (for macOS)

## Introduction

Welcome to this intermediate-level Python tutorial, designed to guide you through building a simple yet functional RESTful API using the Flask web framework. Having completed the previous tutorial, you are already comfortable with Python fundamentals, including functions, basic syntax, and object-oriented programming (OOP). This tutorial will leverage those skills and introduce you to the world of web services, specifically focusing on how to create a REST API.

REST (Representational State Transfer) is an architectural style for distributed hypermedia systems. REST APIs are a common way for different software systems to communicate with each other over the internet. They are stateless, meaning each request from a client to the server contains all the information needed to understand the request, and they typically use standard HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources.

Flask is a lightweight and flexible Python web framework. It's often referred to as a "microframework" because it doesn't include an ORM (Object Relational Mapper) or other functionalities out of the box. This minimalist approach makes Flask easy to get started with and highly customizable, allowing you to choose the tools and libraries that best suit your project.

By the end of this tutorial, you will have built a complete CRUD (Create, Read, Update, Delete) API for a simple ToDo list application. You will understand the core concepts of API development, including handling different HTTP requests, structuring data, and implementing robust error handling. This hands-on experience will provide a solid foundation for building more complex web services in the future.

## What You Will Learn

-   **Setting up a Flask Project:** Initialize a Flask application and understand its basic structure.
-   **Handling HTTP Requests:** Respond to GET, POST, PUT, and DELETE requests.
-   **Returning JSON Data:** Format and send data in JSON format, the standard for web APIs.
-   **Processing Request Data:** Extract and validate data sent by clients.
-   **Structuring Data with OOP:** Use Python classes to represent and manage your API's resources.
-   **Implementing CRUD Operations:** Build a complete API that allows clients to create, read, update, and delete resources.
-   **API Design Best Practices:** Understand principles like endpoints, HTTP status codes, and idempotency.

## Setup Guide (macOS)

This tutorial assumes you are working on a macOS environment. We will use the Terminal for commands, `python3` for running Python scripts, `pip` for package management, and `curl` for testing our API endpoints. If you are on a different operating system, the Python and `pip` commands will be similar, but shell commands might vary slightly.

### Step 1: Verify Python 3 Installation

macOS typically comes with Python pre-installed, but it might be an older version. Ensure you have Python 3.8 or newer. Open your Terminal (you can find it in `Applications/Utilities/Terminal.app` or by searching with Spotlight `Cmd + Space` and typing "Terminal").

Run the following command to check your Python version:

```bash
python3 --version
```

You should see an output similar to `Python 3.x.x`. If you don't have Python 3 or have an older version, it's recommended to install it via Homebrew (a package manager for macOS) or from the official Python website.

**Using Homebrew (Recommended for macOS):**

If you don't have Homebrew, install it first:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Python 3:

```bash
brew install python
```

### Step 2: Create a Project Directory

It's good practice to organize your projects. Create a new directory for our API project:

```bash
mkdir flask_todo_api
cd flask_todo_api
```

### Step 3: Create and Activate a Virtual Environment

Virtual environments are crucial for Python development. They create an isolated environment for your project's dependencies, preventing conflicts with other projects or your system's Python installation.

Create a virtual environment named `venv`:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Your terminal prompt should now show `(venv)` at the beginning, indicating that the virtual environment is active.

### Step 4: Install Flask

With your virtual environment activated, install Flask using `pip`:

```bash
pip install Flask
```

### Step 5: How to Use This Tutorial

-   **Follow Along:** Type out the code examples yourself. This helps with muscle memory and understanding.
-   **Experiment:** Don't hesitate to modify the code, try different inputs, and observe the output. This is how you learn best.
-   **Use `curl`:** We will use `curl` extensively to test our API endpoints. `curl` is a command-line tool for making HTTP requests. You can find its documentation here: [https://curl.se/docs/](https://curl.se/docs/)
-   **Text Editor:** Use your preferred text editor (e.g., VS Code, Sublime Text, Atom) to write your Python code.

With your environment set up, let's dive into building our first Flask API!



## Step 1: Installing Flask and Setting Up a Minimal API

### Purpose

The goal of this step is to get a basic Flask application up and running. This "Hello, World!" example will serve as the foundation for all subsequent steps, ensuring your environment is correctly configured and you understand the absolute basics of a Flask web server.

### Concepts Learned

-   **Flask Installation:** How to install the Flask library using `pip`.
-   **`Flask` Class:** The core Flask application object.
-   **`@app.route()` Decorator:** How to define URL routes that map to Python functions.
-   **`return` Statement:** How a Flask view function sends a response back to the client.
-   **`app.run()`:** How to start the Flask development server.

### Example Code: `hello_world.py`

Create a file named `hello_world.py` in your `flask_todo_api` project directory and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

### How to Run It

1.  **Activate your virtual environment** (if you haven't already):

    ```bash
    cd flask_todo_api
    source venv/bin/activate
    ```

2.  **Run the Flask application** from your terminal. Make sure you are in the `flask_todo_api` directory where `hello_world.py` is located:

    ```bash
    python hello_world.py
    ```

    You should see output similar to this:

    ```
     * Serving Flask app 'hello_world'
     * Debug mode: on
     * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: XXX-XXX-XXX
    ```

    This indicates that your Flask development server is running and listening for requests on `http://127.0.0.1:5000` (which is `localhost` on port `5000`).

3.  **Test the API using `curl`** in a *new* terminal window (keep the Flask server running in the first terminal):

    ```bash
    curl http://127.0.0.1:5000/
    ```

    You should see the response:

    ```
    Hello, World!
    ```

    You can also open `http://127.0.0.1:5000/` in your web browser to see the same message.

### Explanations and Best Practices

-   **`from flask import Flask`**: This line imports the `Flask` class from the `flask` package.
-   **`app = Flask(__name__)`**: This creates an instance of the `Flask` class. `__name__` is a special Python variable that gets the name of the current module. Flask uses this to know where to look for resources like templates and static files.
-   **`@app.route("/")`**: This is a decorator that tells Flask which URL should trigger our `hello_world` function. In this case, `/` represents the root URL of our application.
-   **`def hello_world():`**: This is our *view function*. When a client requests the `/` URL, this function is executed, and its return value is sent back as the HTTP response.
-   **`app.run(debug=True)`**: This starts the Flask development server. `debug=True` enables debug mode, which provides several benefits:
    -   It activates the debugger, which is helpful for troubleshooting errors.
    -   It enables auto-reloading: the server will automatically restart when you make changes to your code, so you don't have to manually stop and start it.
    -   **Important:** `debug=True` should **never** be used in a production environment due to security risks.
-   **Default Host and Port:** By default, Flask runs on `127.0.0.1` (localhost) and port `5000`. You can change these by passing `host` and `port` arguments to `app.run()`, e.g., `app.run(host='0.0.0.0', port=8000)`.

### Exercises/Improvement Tips

1.  **Change the Port:** Modify `app.run()` to run the application on a different port, e.g., `8000`. Test it with `curl`.
2.  **Return Different Text:** Change the `hello_world` function to return a different greeting or a simple HTML tag (e.g., `<h1>Welcome to my API!</h1>`).
3.  **Add Another Route:** Create a new route, for example, `/about`, that returns a message like "This is a simple Flask API.". Test it with `curl`.

Once you're done experimenting, press `Ctrl+C` in the terminal running the Flask server to stop it.



## Step 2: Handling GET Requests and Returning JSON

### Purpose

Most REST APIs are designed to serve data. In this step, you will learn how to handle `GET` requests, which are used to retrieve data from the server. You will also learn how to return data in JSON (JavaScript Object Notation) format, which is the standard data interchange format for web APIs.

### Concepts Learned

-   **HTTP `GET` Method:** The fundamental method for retrieving resources.
-   **`jsonify` Function:** A Flask utility to convert Python dictionaries into JSON responses.
-   **Lists of Dictionaries:** A common Python data structure used to represent collections of structured data, which translates naturally to JSON arrays of objects.
-   **HTTP Status Codes:** Understanding `200 OK` for successful responses.

### Example Code: `app.py` (Updated)

Let's create a new file named `app.py` for our main application code. This will be the file we continue to modify throughout the tutorial. We'll start by creating a simple in-memory list of items and an endpoint to retrieve them.

Create `app.py` in your `flask_todo_api` directory:

```python
from flask import Flask, jsonify

app = Flask(__name__)

# In-memory data store for our items
items = [
    {"id": 1, "name": "Item A", "description": "First item"},
    {"id": 2, "name": "Item B", "description": "Second item"}
]

@app.route("/items", methods=["GET"])
def get_items():
    """Returns a list of all items."""
    return jsonify(items)

@app.route("/", methods=["GET"])
def hello_world():
    """Returns a simple greeting."""
    return "Hello, World! This is our API."

if __name__ == "__main__":
    app.run(debug=True)
```

### How to Run It

1.  **Activate your virtual environment** (if not already active):

    ```bash
    cd flask_todo_api
    source venv/bin/activate
    ```

2.  **Run the Flask application**:

    ```bash
    python app.py
    ```

    You should see the Flask development server start up, similar to Step 1.

3.  **Test the API using `curl`** in a *new* terminal window:

    **a. Test the root endpoint:**

    ```bash
    curl http://127.0.0.1:5000/
    ```

    Expected output:

    ```
    Hello, World! This is our API.
    ```

    **b. Test the `/items` endpoint:**

    ```bash
    curl http://127.0.0.1:5000/items
    ```

    Expected output (formatted for readability):

    ```json
    [
        {
            "description": "First item",
            "id": 1,
            "name": "Item A"
        },
        {
            "description": "Second item",
            "id": 2,
            "name": "Item B"
        }
    ]
    ```

### Explanations and Best Practices

-   **`from flask import Flask, jsonify`**: We now import `jsonify` in addition to `Flask`. `jsonify` is a helper function that serializes Python dictionaries or lists into JSON format and sets the appropriate `Content-Type` header (`application/json`) in the HTTP response.
-   **`items = [...]`**: This is our simple in-memory data store. In a real-world application, this data would typically come from a database (like SQLite, PostgreSQL, or MongoDB). For this tutorial, an in-memory list of dictionaries is sufficient to demonstrate API concepts.
-   **`@app.route("/items", methods=["GET"])`**: We specify `methods=["GET"]` to explicitly state that this route should only respond to `GET` requests. While Flask defaults to `GET` if `methods` is not specified, it's good practice to be explicit for clarity and to prevent unintended access via other HTTP methods.
-   **`return jsonify(items)`**: This line takes our Python list of dictionaries (`items`) and converts it into a JSON array, which is then sent as the response body. Flask automatically sets the HTTP status code to `200 OK` by default for successful responses.
-   **JSON Structure:** Notice how Python lists map to JSON arrays (`[]`) and Python dictionaries map to JSON objects (`{}`). This natural mapping makes Python and Flask excellent choices for building JSON-based APIs.
-   **HTTP Status Codes:** A `200 OK` status code indicates that the request was successful and the server has returned the requested data. We will explore other status codes in later steps.

### Exercises/Improvement Tips

1.  **Add More Data:** Add a few more items to the `items` list with different `id`, `name`, and `description` values. Test the `/items` endpoint again.
2.  **Filter Data (Challenge):** Implement a new route, e.g., `/items/search`, that accepts a query parameter (e.g., `?name=Item`) and returns only items whose name contains the search term. You'll need to import `request` from Flask and use `request.args.get('name')` to get the query parameter.

    *Hint: You might need to use a list comprehension or a loop to filter the `items` list.*

3.  **Return a Single Item (Challenge):** Create a new route, e.g., `/items/<int:item_id>`, that returns a single item based on its `id`. If the item is not found, it should return an appropriate error message and status code (e.g., `404 Not Found`). We will cover error handling more formally in a later step, but you can try to implement a basic version now. You'll need to iterate through the `items` list to find the matching `id`.



## Step 3: Accepting POST Requests and Processing Data

### Purpose

So far, our API can only retrieve data using `GET` requests. In this step, you will learn how to enable your API to receive data from clients using `POST` requests. `POST` requests are typically used to create new resources on the server. We will implement an endpoint that allows clients to add new items to our in-memory data store.

### Concepts Learned

-   **HTTP `POST` Method:** The method used to send data to the server to create a new resource.
-   **`request` Object:** Flask's global request object, which provides access to incoming request data.
-   **`request.json`:** How to parse incoming JSON data from the request body.
-   **Generating IDs:** A simple way to assign unique IDs to new resources.
-   **HTTP Status Code `201 Created`:** The appropriate status code for successful resource creation.

### Example Code: `app.py` (Updated)

We will modify our `app.py` file to include a new route for handling `POST` requests to `/items`. This route will expect JSON data in the request body, extract the `name` and `description` for the new item, assign a unique ID, and add it to our `items` list.

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for our items
items = [
    {"id": 1, "name": "Item A", "description": "First item"},
    {"id": 2, "name": "Item B", "description": "Second item"}
]

# Simple counter for generating new IDs
next_id = 3

@app.route("/items", methods=["GET"])
def get_items():
    """Returns a list of all items."""
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    """Adds a new item to the list."""
    global next_id # Declare that we are modifying the global next_id variable

    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    if "name" not in request.json or "description" not in request.json:
        return jsonify({"error": "Missing 'name' or 'description'"}), 400

    new_item = {
        "id": next_id,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201 # 201 Created status code

@app.route("/", methods=["GET"])
def hello_world():
    """Returns a simple greeting."""
    return "Hello, World! This is our API."

if __name__ == "__main__":
    app.run(debug=True)
```

### How to Run It

1.  **Stop your Flask server** if it's currently running (`Ctrl+C` in the terminal where it's running).
2.  **Run the updated Flask application**:

    ```bash
    python app.py
    ```

3.  **Test adding a new item using `curl`** in a *new* terminal window:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Item C", "description": "Third item"}' http://127.0.0.1:5000/items
    ```

    Expected output (formatted for readability):

    ```json
    {
        "description": "Third item",
        "id": 3,
        "name": "Item C"
    }
    ```

4.  **Verify the new item was added** by making a `GET` request to `/items`:

    ```bash
    curl http://127.0.0.1:5000/items
    ```

    You should now see "Item C" in the list of items.

5.  **Test with missing data (error handling):**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Item D"}' http://127.0.0.1:5000/items
    ```

    Expected output:

    ```json
    {
        "error": "Missing 'name' or 'description'"
    }
    ```

    And the HTTP status code will be `400 Bad Request` (you can verify this by adding `-v` to your `curl` command: `curl -v -X POST ...`).

### Explanations and Best Practices

-   **`from flask import Flask, jsonify, request`**: We now import the `request` object, which is essential for accessing incoming request data.
-   **`methods=["POST"]`**: This explicitly tells Flask that this route should only handle `POST` requests.
-   **`global next_id`**: Since we are modifying `next_id` (incrementing it), we need to declare it as `global` within the `add_item` function. This tells Python that we are referring to the `next_id` variable defined outside the function, not creating a new local one.
-   **`if not request.json:`**: This checks if the incoming request body contains valid JSON data. If the `Content-Type` header is not `application/json` or the body is not valid JSON, `request.json` will be `None`.
-   **`if "name" not in request.json or "description" not in request.json:`**: This performs basic validation to ensure that the required fields (`name` and `description`) are present in the incoming JSON data. If they are missing, we return an error message and a `400 Bad Request` status code.
-   **`new_item = {...}`**: We construct a new dictionary for the item, assigning it a unique `id` using our `next_id` counter and extracting `name` and `description` from `request.json`.
-   **`items.append(new_item)`**: The new item is added to our in-memory list.
-   **`return jsonify(new_item), 201`**: We return the newly created item as JSON and explicitly set the HTTP status code to `201 Created`. This status code is crucial for `POST` requests as it informs the client that a new resource has been successfully created on the server.
-   **Request Body and Content Types:** For `POST` (and `PUT`) requests, the data is typically sent in the *request body*. The `Content-Type` header is vital as it tells the server how to interpret the data in the body. For JSON data, it should always be `application/json`.

### Exercises/Improvement Tips

1.  **Input Validation Enhancement:** Add more robust validation to the `add_item` function. For example, ensure that the `name` and `description` are not empty strings after stripping whitespace. Return a `400 Bad Request` if they are.
2.  **Unique Names (Challenge):** Modify `add_item` to prevent adding items with duplicate names. If a name already exists, return a `409 Conflict` status code with an appropriate error message.
3.  **Add More Fields:** Extend the `new_item` dictionary to include other fields, such as `status` (e.g., "pending", "completed") or `due_date`. Ensure these fields are also validated if necessary. Test adding items with these new fields.))




## Step 4: Adding Multiple Routes and Handling Errors

### Purpose

In a real-world API, you'll need more than just a single endpoint for all operations. This step focuses on creating more specific routes, particularly for retrieving individual resources. We will also introduce proper error handling, which is crucial for building robust APIs that gracefully respond to invalid requests or missing resources.

### Concepts Learned

-   **Route Parameters:** How to define dynamic parts in your URLs to retrieve specific resources (e.g., an item by its ID).
-   **HTTP `GET` for Specific Resources:** Using `GET` with a parameter to fetch a single item.
-   **Error Handling with `abort`:** How to immediately stop a request and return an HTTP error response.
-   **`errorhandler` Decorator:** How to define custom error pages or JSON responses for specific HTTP error codes (e.g., `404 Not Found`).
-   **HTTP Status Code `404 Not Found`:** The standard status code for when a requested resource does not exist.

### Example Code: `app.py` (Updated)

We will add a new route `/items/<int:item_id>` to retrieve a single item by its ID. We'll also implement error handling for when an item is not found.

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data store for our items
items = [
    {"id": 1, "name": "Item A", "description": "First item"},
    {"id": 2, "name": "Item B", "description": "Second item"}
]

# Simple counter for generating new IDs
next_id = 3

@app.route("/items", methods=["GET"])
def get_items():
    """Returns a list of all items."""
    return jsonify(items)

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """Returns a single item by its ID."""
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404) # Abort with a 404 Not Found error
    return jsonify(item)

@app.route("/items", methods=["POST"])
def add_item():
    """Adds a new item to the list."""
    global next_id

    if not request.json:
        abort(400) # Bad Request
    if "name" not in request.json or "description" not in request.json:
        abort(400) # Bad Request

    new_item = {
        "id": next_id,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    items.append(new_item)
    next_id += 1
    return jsonify(new_item), 201 # 201 Created status code

# Custom error handler for 404 Not Found errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "The requested resource was not found."}), 404

# Custom error handler for 400 Bad Request errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": "The request was malformed or missing required parameters."}), 400

@app.route("/", methods=["GET"])
def hello_world():
    """Returns a simple greeting."""
    return "Hello, World! This is our API."

if __name__ == "__main__":
    app.run(debug=True)
```

### How to Run It

1.  **Stop your Flask server** if it's currently running (`Ctrl+C`).
2.  **Run the updated Flask application**:

    ```bash
    python app.py
    ```

3.  **Test retrieving a specific item using `curl`**:

    ```bash
    curl http://127.0.0.1:5000/items/1
    ```

    Expected output (for Item A):

    ```json
    {
        "description": "First item",
        "id": 1,
        "name": "Item A"
    }
    ```

4.  **Test retrieving a non-existent item**:

    ```bash
    curl http://127.0.0.1:5000/items/99
    ```

    Expected output (our custom 404 error):

    ```json
    {
        "error": "Not Found",
        "message": "The requested resource was not found."
    }
    ```

5.  **Test the `POST` request with missing data again** to see the custom 400 error:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d 
    ```

    Expected output:

    ```json
    {
        "error": "Bad Request",
        "message": "The request was malformed or missing required parameters."
    }
    ```

### Explanations and Best Practices

-   **`from flask import Flask, jsonify, request, abort`**: We've added `abort` to our imports. The `abort` function is used to immediately stop the execution of a request and return an HTTP error response.
-   **`@app.route("/items/<int:item_id>", methods=["GET"])`**: This new route definition includes a *variable part* in the URL: `<int:item_id>`. The `<int:>` part is a converter that ensures the `item_id` captured from the URL path is an integer. This `item_id` is then passed as an argument to the `get_item` function.
-   **`item = next((item for item in items if item["id"] == item_id), None)`**: This is a concise way to find an item in our `items` list by its `id`. `next()` attempts to get the next item from the generator expression. If no item matches, it returns `None` (the second argument).
-   **`if item is None: abort(404)`**: If the item is not found, we call `abort(404)`. This raises an `HTTPException` with a 404 status code. Flask then looks for an error handler for this status code.
-   **`@app.errorhandler(404)` and `@app.errorhandler(400)`**: These decorators register functions to handle specific HTTP error codes. When `abort(404)` is called, Flask will execute our `not_found` function, which returns a custom JSON error message and the `404 Not Found` status code. Similarly, `bad_request` handles `400 Bad Request` errors.
-   **RESTful Principles - Resource Identification:** Using `/items` for the collection of items and `/items/{item_id}` for a specific item is a fundamental RESTful pattern for identifying resources. This makes your API predictable and easy to understand.
-   **Custom Error Messages:** Providing clear, consistent, and machine-readable error messages (like JSON objects with `error` and `message` fields) is a best practice. It helps API consumers understand what went wrong and how to fix their requests.

### Exercises/Improvement Tips

1.  **Implement `400 Bad Request` for `POST`:** Ensure that if the `name` or `description` fields are empty strings (after stripping whitespace) in a `POST` request, you also `abort(400)` with a clear message.
2.  **Add a `500 Internal Server Error` Handler:** While Flask handles unhandled exceptions with a 500 error by default, it's good practice to have a custom handler. Create an `@app.errorhandler(500)` that returns a generic JSON error message, avoiding exposing sensitive server details.
3.  **Search by Name (Challenge):** Extend the `/items` route to allow searching by name using a query parameter, e.g., `/items?name=Item`. If the `name` query parameter is present, filter the results. If not, return all items. Remember to use `request.args.get('name')` to access query parameters. If no items match the search, return an empty list `[]` and a `200 OK` status, as this is a successful query with no results, not an error.



## Step 5: Using Classes for Structuring Data (e.g., a Simple ToDo List)

### Purpose

As our API grows, managing data as simple dictionaries in a global list becomes cumbersome and less maintainable. This step introduces how to use Python classes to structure our data, making our code more organized, readable, and easier to extend. We will create a `Todo` class to represent individual to-do items and a `TodoManager` class to handle the collection of these items, encapsulating data management logic.

### Concepts Learned

-   **Object-Oriented Programming (OOP) Review:** Applying classes and objects to model real-world entities.
-   **Class Definition:** Defining a `Todo` class with attributes (id, title, description, completed).
-   **Instance Management:** How to create, store, and retrieve instances of our `Todo` class.
-   **Encapsulation:** Bundling data (attributes) and methods (functions) that operate on the data within a single unit (the class).
-   **`__init__` Method:** The constructor for our `Todo` class.
-   **`to_dict()` Method:** A common pattern in API development to convert an object instance into a dictionary, which can then be easily `jsonify`-ed.

### Example Code: `app.py` (Updated with Classes)

We will refactor our `app.py` to use `Todo` objects instead of raw dictionaries. This involves creating a `Todo` class and modifying our `items` list to store `Todo` instances. We will also introduce a `TodoManager` class to handle the operations on our `Todo` items.

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# --- Todo Class Definition ---
class Todo:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        """Converts the Todo object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

# --- TodoManager Class Definition ---
class TodoManager:
    def __init__(self):
        self.todos = []
        self.next_id = 1
        # Initialize with some dummy data
        self.add_todo("Learn Flask", "Understand the basics of Flask framework.")
        self.add_todo("Build API", "Create a RESTful API for a ToDo list.")

    def add_todo(self, title, description, completed=False):
        if not title or not description:
            return None # Or raise an error
        todo = Todo(self.next_id, title, description, completed)
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def get_all_todos(self):
        return [todo.to_dict() for todo in self.todos]

    def get_todo_by_id(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo.to_dict()
        return None

    # Placeholder for update and delete, to be implemented in next step
    def update_todo(self, todo_id, new_data):
        # This will be implemented in the next step
        pass

    def delete_todo(self, todo_id):
        # This will be implemented in the next step
        pass

# Instantiate our TodoManager
todo_manager = TodoManager()

# --- API Routes (Modified to use TodoManager) ---

@app.route("/todos", methods=["GET"])
def get_todos():
    """Returns a list of all todos."""
    return jsonify(todo_manager.get_all_todos())

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    """Returns a single todo by its ID."""
    todo = todo_manager.get_todo_by_id(todo_id)
    if todo is None:
        abort(404) # Not Found
    return jsonify(todo)

@app.route("/todos", methods=["POST"])
def create_todo():
    """Creates a new todo item."""
    if not request.json:
        abort(400) # Bad Request
    if "title" not in request.json or "description" not in request.json:
        abort(400) # Bad Request

    title = request.json["title"]
    description = request.json["description"]
    completed = request.json.get("completed", False) # Allow optional 'completed' field

    new_todo = todo_manager.add_todo(title, description, completed)
    if new_todo is None:
        abort(400, description="Failed to create todo. Title or description might be empty.")

    return jsonify(new_todo.to_dict()), 201 # 201 Created

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
```

### How to Run It

1.  **Stop your Flask server** if it's currently running (`Ctrl+C`).
2.  **Replace the content of your `app.py`** file with the updated code above. This is a significant refactoring, so it's best to replace the entire file content.
3.  **Run the updated Flask application**:

    ```bash
    python app.py
    ```

4.  **Test retrieving all todos**:

    ```bash
    curl http://127.0.0.1:5000/todos
    ```

    You should see the initial two todo items:

    ```json
    [
        {
            "id": 1,
            "title": "Learn Flask",
            "description": "Understand the basics of Flask framework.",
            "completed": false
        },
        {
            "id": 2,
            "title": "Build API",
            "description": "Create a RESTful API for a ToDo list.",
            "completed": false
        }
    ]
    ```

5.  **Test retrieving a specific todo**:

    ```bash
    curl http://127.0.0.1:5000/todos/1
    ```

    Expected output:

    ```json
    {
        "id": 1,
        "title": "Learn Flask",
        "description": "Understand the basics of Flask framework.",
        "completed": false
    }
    ```

6.  **Test creating a new todo**:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Buy Groceries", "description": "Milk, Eggs, Bread"}' http://127.0.0.1:5000/todos
    ```

    Expected output (with the new todo item):

    ```json
    {
        "completed": false,
        "description": "Milk, Eggs, Bread",
        "id": 3,
        "title": "Buy Groceries"
    }
    ```

7.  **Verify the new todo was added**:

    ```bash
    curl http://127.0.0.1:5000/todos
    ```

    You should now see three todo items.

### Explanations and Best Practices

-   **`Todo` Class:**
    -   The `__init__` method now takes `id`, `title`, `description`, and an optional `completed` status. This makes each `Todo` object a self-contained unit of data.
    -   The `to_dict()` method is crucial. Flask's `jsonify` function works best with dictionaries. By implementing `to_dict()`, we provide a clean way to convert our `Todo` object into a dictionary format that can be easily serialized to JSON.
-   **`TodoManager` Class:**
    -   This class centralizes all logic related to managing our collection of `Todo` objects. It holds the `todos` list and handles operations like adding, retrieving, updating, and deleting (which we'll implement next).
    -   **Encapsulation:** The `TodoManager` encapsulates the internal representation of our todos (the `todos` list and `next_id`) and exposes methods (`add_todo`, `get_all_todos`, `get_todo_by_id`) to interact with them. This separates concerns and makes the code more modular.
    -   **Data Integrity:** By having `add_todo` handle ID generation, we ensure that each new todo gets a unique ID, preventing accidental duplicates.
-   **Refactored Routes:**
    -   Our API routes (`/todos`, `/todos/<int:todo_id>`) now interact with the `todo_manager` instance instead of directly manipulating a global `items` list. This makes the routes cleaner and delegates data management to the `TodoManager`.
    -   Notice how `get_todos()` calls `todo_manager.get_all_todos()`, which in turn uses a list comprehension to call `to_dict()` on each `Todo` object before `jsonify`-ing the result.
    -   The `create_todo()` function now uses `todo_manager.add_todo()` to create a new `Todo` object and handles the optional `completed` field using `request.json.get("completed", False)`.
-   **Error Handling Refinement:** We've updated the `abort(400)` calls to include a `description` argument. This description is then used in our custom `errorhandler` functions, providing more specific error messages to the client.

### Exercises/Improvement Tips

1.  **Add Validation to `TodoManager.add_todo`:** Currently, `add_todo` returns `None` if `title` or `description` are empty. Modify it to raise a `ValueError` instead, and then catch this `ValueError` in `create_todo()` and return a `400 Bad Request` with a specific error message.
2.  **Implement `TodoManager.update_todo` (Partial):** Start implementing the `update_todo` method in `TodoManager`. It should take `todo_id` and `new_data` (a dictionary) as arguments. Find the `Todo` object by `todo_id` and update its `title`, `description`, and `completed` attributes based on `new_data`. For now, just print a message indicating success or failure.
3.  **Implement `TodoManager.delete_todo` (Partial):** Similarly, start implementing the `delete_todo` method. It should take `todo_id` as an argument, find the `Todo` object, and remove it from the `self.todos` list. Print a message indicating success or failure.
4.  **Add a `__repr__` Method to `Todo`:** Implement a `__repr__` method in the `Todo` class to provide a more developer-friendly string representation of the object, useful for debugging (e.g., `Todo(id=1, title='Learn Flask')`).



## Step 6: Completing a Basic CRUD API

### Purpose

Now that we have the ability to create and read (retrieve) our to-do items, it's time to complete the full CRUD (Create, Read, Update, Delete) functionality of our API. In this step, you will learn how to implement `PUT` requests for updating existing resources and `DELETE` requests for removing them. This will make our API fully functional for managing to-do items.

### Concepts Learned

-   **HTTP `PUT` Method:** Used to update an existing resource. `PUT` is typically idempotent, meaning that making the same `PUT` request multiple times will have the same effect as making it once.
-   **HTTP `DELETE` Method:** Used to remove a specified resource.
-   **Request Parsing for Updates:** How to extract data from the request body for updating an existing resource.
-   **HTTP Status Code `200 OK` (for successful updates/deletions):** Indicates that the request was successful.
-   **HTTP Status Code `204 No Content` (for successful deletions with no response body):** Often used for `DELETE` requests when there's no content to return.

### Example Code: `app.py` (Updated with CRUD)

We will now complete the `update_todo` and `delete_todo` methods in our `TodoManager` class and add corresponding `PUT` and `DELETE` routes to our Flask application.

```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# --- Todo Class Definition ---
class Todo:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        """Converts the Todo object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    def update_from_dict(self, data):
        """Updates the Todo object attributes from a dictionary."""
        if "title" in data: self.title = data["title"]
        if "description" in data: self.description = data["description"]
        if "completed" in data: self.completed = data["completed"]

# --- TodoManager Class Definition ---
class TodoManager:
    def __init__(self):
        self.todos = []
        self.next_id = 1
        # Initialize with some dummy data
        self.add_todo("Learn Flask", "Understand the basics of Flask framework.")
        self.add_todo("Build API", "Create a RESTful API for a ToDo list.")

    def add_todo(self, title, description, completed=False):
        if not title or not description:
            return None # Or raise an error, as discussed in exercises
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
        return None

    def update_todo(self, todo_id, new_data):
        """Updates an existing todo item."""
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            return None # Todo not found

        # Basic validation for update data
        if not new_data:
            return None # No data provided for update

        todo.update_from_dict(new_data)
        return todo.to_dict()

    def delete_todo(self, todo_id):
        """Deletes a todo item by ID."""
        original_len = len(self.todos)
        self.todos = [todo for todo in self.todos if todo.id != todo_id]
        return len(self.todos) < original_len # True if an item was removed

# Instantiate our TodoManager
todo_manager = TodoManager()

# --- API Routes (Updated with PUT and DELETE) ---

@app.route("/todos", methods=["GET"])
def get_todos():
    """Returns a list of all todos."""
    return jsonify(todo_manager.get_all_todos())

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    """Returns a single todo by its ID."""
    todo = todo_manager.get_todo_by_id(todo_id)
    if todo is None:
        abort(404) # Not Found
    return jsonify(todo.to_dict())

@app.route("/todos", methods=["POST"])
def create_todo():
    """Creates a new todo item."""
    if not request.json:
        abort(400, description="Request must be JSON.")
    if "title" not in request.json or "description" not in request.json:
        abort(400, description="Missing \'title\' or \'description\'.")

    title = request.json["title"]
    description = request.json["description"]
    completed = request.json.get("completed", False)

    new_todo = todo_manager.add_todo(title, description, completed)
    if new_todo is None:
        abort(400, description="Failed to create todo. Title or description might be empty.")

    return jsonify(new_todo.to_dict()), 201 # 201 Created

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    """Updates an existing todo item."""
    if not request.json:
        abort(400, description="Request must be JSON.")

    updated_todo = todo_manager.update_todo(todo_id, request.json)
    if updated_todo is None:
        abort(404) # Not Found

    return jsonify(updated_todo), 200 # 200 OK

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    """Deletes a todo item."""
    if not todo_manager.delete_todo(todo_id):
        abort(404) # Not Found

    return 
```

### How to Run It

1.  **Stop your Flask server** if it's currently running (`Ctrl+C`).
2.  **Replace the content of your `app.py`** file with the updated code above.
3.  **Run the updated Flask application**:

    ```bash
    python app.py
    ```

4.  **Test updating an item using `curl`**:

    First, ensure you have an item with ID 1 (e.g., "Learn Flask").

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Learn Flask (Updated)", "completed": true}' http://127.0.0.1:5000/todos/1
    ```

    Expected output:

    ```json
    {
        "completed": true,
        "description": "Understand the basics of Flask framework.",
        "id": 1,
        "title": "Learn Flask (Updated)"
    }
    ```

    Verify the update:

    ```bash
    curl http://127.0.0.1:5000/todos/1
    ```

5.  **Test deleting an item using `curl`**:

    ```bash
    curl -X DELETE http://127.0.0.1:5000/todos/2
    ```

    Expected output (empty response, 204 No Content status):

    ```
    
    ```

    Verify the deletion:

    ```bash
    curl http://127.0.0.1:5000/todos
    ```

    You should now only see the updated "Learn Flask" item and any new items you've added.

6.  **Test updating a non-existent item**:

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Non Existent"}' http://127.0.0.1:5000/todos/99
    ```

    Expected output (404 Not Found):

    ```json
    {
        "error": "Not Found",
        "message": "The requested resource was not found."
    }
    ```

7.  **Test deleting a non-existent item**:

    ```bash
    curl -X DELETE http://127.0.0.1:5000/todos/99
    ```

    Expected output (404 Not Found):

    ```json
    {
        "error": "Not Found",
        "message": "The requested resource was not found."
    }
    ```

### Explanations and Best Practices

-   **`Todo.update_from_dict(self, data)`:** This new method in the `Todo` class allows us to update the attributes of a `Todo` object based on a dictionary of new data. It checks if the keys (`title`, `description`, `completed`) exist in the `data` dictionary before updating, allowing for partial updates.
-   **`TodoManager.update_todo(self, todo_id, new_data)`:**
    -   It first retrieves the `Todo` object using `get_todo_by_id`.
    -   If the todo is found, it calls the `update_from_dict` method on the `Todo` object.
    -   It returns the updated todo as a dictionary or `None` if not found or no data provided.
-   **`TodoManager.delete_todo(self, todo_id)`:**
    -   This method uses a list comprehension to create a new list of todos, excluding the one with the matching `todo_id`.
    -   It returns `True` if an item was removed (i.e., the length of the list changed), and `False` otherwise.
-   **`@app.route("/todos/<int:todo_id>", methods=["PUT"])`:**
    -   This route handles `PUT` requests to a specific todo resource (identified by `todo_id`).
    -   It expects JSON data in the request body, which contains the fields to be updated.
    -   It calls `todo_manager.update_todo` and returns the updated todo with a `200 OK` status, or `404 Not Found` if the todo doesn't exist.
-   **`@app.route("/todos/<int:todo_id>", methods=["DELETE"])`:**
    -   This route handles `DELETE` requests for a specific todo resource.
    -   It calls `todo_manager.delete_todo`.
    -   If the deletion is successful, it returns an empty response with a `204 No Content` status code. This is a common practice for `DELETE` requests where no content needs to be returned to the client. If the todo is not found, it returns `404 Not Found`.
-   **Idempotency of `PUT`:** A `PUT` request is idempotent. If you send the same `PUT` request multiple times, the state of the resource on the server will be the same as if you sent it once. This is because `PUT` is used to *replace* a resource or *create* it if it doesn't exist at the specified URI. In our case, we are updating an existing resource.

### Exercises/Improvement Tips

1.  **Partial Updates (`PATCH`):** Currently, our `PUT` endpoint expects the full resource data. Implement a `PATCH` endpoint (`@app.route("/todos/<int:todo_id>", methods=["PATCH"])`) that allows for partial updates. For example, a client might only want to update the `completed` status without sending the `title` or `description`.
2.  **More Robust Validation for `PUT`:** Add more validation to the `update_todo` function in `TodoManager` and the `update_todo` route. For instance, ensure that `title` and `description` are not empty strings if they are provided in the update data.
3.  **Error Handling for Invalid Update Data:** If a client sends invalid data types for update (e.g., `"completed": "yes"` instead of `true`/`false`), how would you handle this and return a `400 Bad Request`? (Hint: You might need to add more checks in `Todo.update_from_dict` or before calling it.)
4.  **Add a `GET` endpoint for `completed` todos:** Create a new route, e.g., `/todos/completed`, that returns only the todos where `completed` is `True`.



## Step 7: Explaining API Design Basics

### Purpose

Building a functional API is one thing; building a *well-designed* API is another. This step will consolidate your understanding of fundamental RESTful API design principles. A well-designed API is intuitive, consistent, and easy for other developers to use, which is crucial for its adoption and long-term maintainability. We will review key concepts like endpoints, HTTP methods, status codes, and the characteristics of a RESTful API.

### Concepts Learned

-   **REST Principles:** Understanding the core tenets of Representational State Transfer.
-   **HTTP Methods (Verbs):** A deeper dive into GET, POST, PUT, DELETE, and their intended uses.
-   **HTTP Status Codes:** A comprehensive overview of common status codes and their meanings.
-   **Idempotency:** The property of certain HTTP methods that ensures multiple identical requests have the same effect as a single request.
-   **Statelessness:** The principle that each request from a client to a server must contain all the information needed to understand the request.
-   **Endpoints:** The specific URLs that represent resources in your API.
-   **Versioning (Briefly):** Why and how APIs are versioned.
-   **Authentication (Briefly):** How APIs secure access.

### Explanations and Best Practices

#### 1. REST Principles

REST is an architectural style, not a strict protocol. It defines a set of constraints for how a distributed system should behave. The core principles include:

-   **Client-Server:** Separation of concerns between the client (frontend, mobile app) and the server (backend API). This improves portability and scalability.
-   **Stateless:** Each request from client to server must contain all the information needed to understand the request. The server should not store any client context between requests. This improves scalability and reliability.
-   **Cacheable:** Responses must explicitly or implicitly define themselves as cacheable or non-cacheable to prevent clients from reusing stale or inappropriate data.
-   **Uniform Interface:** This is the most critical constraint, simplifying the overall system architecture. It involves:
    -   **Resource Identification in Requests:** Individual resources are identified in requests (e.g., `/todos/1`).
    -   **Resource Manipulation through Representations:** Clients manipulate resources using representations (e.g., JSON).
    -   **Self-descriptive Messages:** Each message includes enough information to describe how to process the message.
    -   **Hypermedia as the Engine of Application State (HATEOAS):** Clients interact with the application entirely through hypermedia provided dynamically by server-side applications. (This is an advanced concept often not fully implemented in simpler APIs, but it's a core REST principle).

#### 2. HTTP Methods (Verbs)

HTTP methods, also known as HTTP verbs, indicate the desired action to be performed on the identified resource. Using them correctly is fundamental to a RESTful API:

-   **`GET` (Retrieve):** Used to request data from a specified resource. `GET` requests should only retrieve data and should have no other effect on the data. They are *safe* and *idempotent*.
    -   *Example:* `GET /todos` (get all todos), `GET /todos/1` (get todo with ID 1).
-   **`POST` (Create):** Used to submit an entity to the specified resource, often causing a change in state or the creation of a new resource. `POST` requests are neither safe nor idempotent.
    -   *Example:* `POST /todos` (create a new todo).
-   **`PUT` (Update/Replace):** Used to update a resource or create a resource if it doesn't exist at the specified URI. `PUT` requests are idempotent.
    -   *Example:* `PUT /todos/1` (update todo with ID 1, replacing its entire representation).
-   **`DELETE` (Delete):** Used to delete the specified resource. `DELETE` requests are idempotent.
    -   *Example:* `DELETE /todos/1` (delete todo with ID 1).
-   **`PATCH` (Partial Update):** Used to apply partial modifications to a resource. `PATCH` requests are neither safe nor idempotent in general, though they can be designed to be idempotent.
    -   *Example:* `PATCH /todos/1` (update only the `completed` status of todo with ID 1).

#### 3. HTTP Status Codes

Status codes are three-digit numbers returned by the server in response to a client's request. They indicate whether a specific HTTP request has been successfully completed. Understanding them is crucial for both API developers and consumers.

Here are some common categories and examples:

-   **`1xx` (Informational):** The request was received, continuing process.
-   **`2xx` (Success):** The action was successfully received, understood, and accepted.
    -   `200 OK`: Standard response for successful HTTP requests. (e.g., `GET`, `PUT`, `PATCH`)
    -   `201 Created`: The request has been fulfilled and resulted in a new resource being created. (e.g., `POST`)
    -   `204 No Content`: The server successfully processed the request, but is not returning any content. Often used for `DELETE` requests.
-   **`3xx` (Redirection):** Further action needs to be taken by the user agent to fulfill the request.
-   **`4xx` (Client Error):** The request contains bad syntax or cannot be fulfilled.
    -   `400 Bad Request`: The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
    -   `401 Unauthorized`: Authentication is required and has failed or has not yet been provided.
    -   `403 Forbidden`: The client does not have access rights to the content.
    -   `404 Not Found`: The server can't find the requested resource.
    -   `405 Method Not Allowed`: The request method is known by the server but has been disabled and cannot be used.
    -   `409 Conflict`: Indicates a request conflict with current state of the target resource. (e.g., trying to create a resource that already exists with a unique identifier).
-   **`5xx` (Server Error):** The server failed to fulfill an apparently valid request.
    -   `500 Internal Server Error`: A generic error message, given when an unexpected condition was encountered and no more specific message is suitable.

#### 4. Idempotency

Idempotency means that an operation can be applied multiple times without changing the result beyond the initial application. In the context of HTTP methods:

-   **Idempotent Methods:** `GET`, `HEAD`, `PUT`, `DELETE`, `OPTIONS`, `TRACE`.
    -   Calling `GET /todos/1` multiple times will always retrieve the same todo (assuming no external changes).
    -   Calling `PUT /todos/1` with the same data multiple times will result in the same state for todo 1.
    -   Calling `DELETE /todos/1` multiple times will delete the todo once, and subsequent calls will indicate that the resource is no longer found (but won't cause further changes).
-   **Non-Idempotent Methods:** `POST`, `PATCH`.
    -   Calling `POST /todos` multiple times will typically create multiple new todo items.
    -   Calling `PATCH /todos/1` can be non-idempotent if the patch operation is relative (e.g., "increment value by X").

#### 5. Statelessness

As mentioned, statelessness is a core REST constraint. It means that the server does not store any information about the client's session between requests. Every request from the client to the server must contain all the information necessary to understand the request. This includes authentication tokens, session IDs, or any other context.

**Benefits of Statelessness:**
-   **Scalability:** Easier to scale horizontally as any server can handle any request.
-   **Reliability:** Less prone to errors as there's no session state to get corrupted.
-   **Visibility:** Each request is self-contained, making monitoring and debugging easier.

#### 6. Endpoints

An endpoint is a specific URL where an API can be accessed by a client. It's the point of interaction between the client and the server. Well-designed endpoints are:

-   **Resource-Oriented:** They represent resources (nouns), not actions (verbs). For example, `/todos` is better than `/getAllTodos`.
-   **Hierarchical:** They often follow a logical hierarchy. `/users/123/orders/456`.
-   **Plural Nouns:** Use plural nouns for collections (e.g., `/todos`, `/users`).

#### 7. Versioning (Briefly)

As your API evolves, you might need to make breaking changes. Versioning allows you to introduce new versions of your API without breaking existing client applications. Common versioning strategies include:

-   **URI Versioning:** `api.example.com/v1/todos`
-   **Header Versioning:** `Accept: application/vnd.example.v1+json`
-   **Query Parameter Versioning:** `api.example.com/todos?version=1`

URI versioning is often the simplest and most transparent for consumers.

#### 8. Authentication (Briefly)

For most real-world APIs, you'll need to secure access. Common authentication methods include:

-   **API Keys:** Simple tokens passed in headers or query parameters.
-   **OAuth 2.0:** A widely used standard for delegated authorization, allowing third-party applications to access user data without sharing user credentials.
-   **JWT (JSON Web Tokens):** Compact, URL-safe means of representing claims to be transferred between two parties. Often used with OAuth 2.0.

This concludes our deep dive into API design basics. Understanding these principles will help you build more robust, scalable, and user-friendly APIs.


