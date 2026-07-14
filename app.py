from flask import Flask
from flask_cors import CORS
import os

from config import Config
from database import db

# Import Model
from models.vulnerability import Vulnerability

# Import Routes
from routes.vulnerability import vulnerability_bp

app = Flask(__name__)

CORS(app)

app.config.from_object(Config)

db.init_app(app)

# Create SQLite folder if not exists
os.makedirs("instance", exist_ok=True)

with app.app_context():
    db.create_all()

# Register Blueprint
app.register_blueprint(vulnerability_bp)


@app.route("/")
def home():

    return {
        "message": "Issue & Vulnerability Tracking API Running Successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)