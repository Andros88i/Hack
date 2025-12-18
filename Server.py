from flask import Flask, request, jsonify

app = Flask(__terabox__)

USERS = {
    "admin": "androsgil527@gmail.com",
    "test": "rocaknrrolla1988"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = data.get("user")
    pwd = data.get("pass")

    if USERS.get(user) == pwd:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
