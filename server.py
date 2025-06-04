from flask import Flask, request, jsonify, send_from_directory, redirect
import os
import json

app = Flask(__name__, static_folder=None)

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGIN_DIR = os.path.abspath(os.path.join(BASE_DIR, "../login"))
LANDPAGE_DIR = os.path.abspath(os.path.join(BASE_DIR, "../landpage"))
USERS_FILE = os.path.join(BASE_DIR, "users.json")


# Load or initialize users
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


@app.route("/")
def serve_login():
    return send_from_directory(LOGIN_DIR, "login.html")


@app.route("/login.js")
def serve_js():
    return send_from_directory(LOGIN_DIR, "login.js")


@app.route("/login.css")
def serve_css():
    return send_from_directory(LOGIN_DIR, "login.css")


@app.route("/landpage")
def serve_landpage():
    return send_from_directory(LANDPAGE_DIR, "landpage.html")


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"success": False, "message": "All fields are required"}), 400

    users = load_users()
    if any(u["username"] == username for u in users):
        return jsonify({"success": False, "message": "Username already exists"}), 409

    users.append({"username": username, "email": email, "password": password})
    save_users(users)

    return jsonify({"success": True, "message": "Signup successful"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    users = load_users()
    user = next((u for u in users if u["username"] == username and u["password"] == password), None)

    if user:
        return jsonify({"success": True, "message": "Login successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True, port=3000)
