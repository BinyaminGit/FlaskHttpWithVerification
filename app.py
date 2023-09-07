from flask import Flask, request, jsonify, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# In-memory "databases"
users = {}  # username -> { "password": "hashed_password", "created_at": datetime }
items = {}  # item_id -> { "name": "item_name", "description": "item_description", "created_by": "username" }

@app.before_request
def require_login():
    allowed_routes = ['login', 'register']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return jsonify({"error": "Unauthorized access"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']  # TODO: Hash this in a real-world scenario

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "password": password,
        "created_at": datetime.now().isoformat()
    }

    return jsonify({"message": "User registered"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if username not in users or users[username]['password'] != password:
        return jsonify({"error": "Invalid username or password"}), 401

    session['username'] = username
    return jsonify({"message": "Logged in"}), 200

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({"message": "Logged out"}), 200

@app.route('/item', methods=['POST'])
def create_item():
    data = request.json
    item_id = data['id']
    if item_id in items:
        return jsonify({"error": "Item ID already exists"}), 400

    items[item_id] = {
        "name": data["name"],
        "description": data.get("description", ""),
        "created_by": session['username'],
        "created_at": datetime.now().isoformat()
    }

    return jsonify(items[item_id]), 201

@app.route('/item/<item_id>', methods=['GET'])
def read_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

@app.route('/item/<item_id>', methods=['PUT'])
def update_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    item['updated_at'] = datetime.now().isoformat()

    return jsonify(item), 200

@app.route('/item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    del items[item_id]
    return jsonify({"message": "Item deleted"}), 200

@app.route('/items', methods=['GET'])
def list_items():
    return jsonify(list(items.values())), 200

if __name__ == '__main__':
    app.run(debug=True)
