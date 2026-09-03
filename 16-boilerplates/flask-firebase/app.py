import os
import json
import firebase_admin
from firebase_admin import credentials, auth, firestore
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-to-a-random-string")

# Initialize Firebase Admin SDK
cred_path = os.getenv("FIREBASE_CREDENTIALS", "serviceAccountKey.json")
if os.path.exists(cred_path):
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
else:
    print(f"Warning: {cred_path} not found. Server-side Firebase features disabled.")
    db = None


def login_required(f):
    """Decorator to require authentication for a route."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "uid" not in session:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    if "uid" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user_email=session.get("user_email", ""))


@app.route("/api/verify-token", methods=["POST"])
def verify_token():
    """Verify Firebase ID token sent from client."""
    data = request.get_json()
    id_token = data.get("idToken")

    if not id_token:
        return jsonify({"error": "No token provided"}), 400

    try:
        decoded = auth.verify_id_token(id_token)
        session["uid"] = decoded["uid"]
        session["user_email"] = decoded.get("email", "")
        return jsonify({"status": "ok", "uid": decoded["uid"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 401


@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"status": "ok"})


@app.route("/api/user-data")
@login_required
def user_data():
    """Example: Fetch user data from Firestore."""
    if not db:
        return jsonify({"error": "Firestore not configured"}), 500

    uid = session["uid"]
    doc = db.collection("users").document(uid).get()

    if doc.exists:
        return jsonify(doc.to_dict())
    else:
        return jsonify({"message": "No user data found"}), 404


@app.route("/api/save-data", methods=["POST"])
@login_required
def save_data():
    """Example: Save data to Firestore."""
    if not db:
        return jsonify({"error": "Firestore not configured"}), 500

    data = request.get_json()
    uid = session["uid"]

    db.collection("users").document(uid).set(data, merge=True)
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
