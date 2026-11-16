
from pathlib import Path
from flask import Flask, render_template
from dotenv import load_dotenv

from backend.config import Config
from backend.database import init_db
from backend.routes.chat_routes import chat_bp

ROOT_DIR = Path(__file__).resolve().parent.parent


def create_app():
    load_dotenv(ROOT_DIR / ".env")

    app = Flask(
        __name__,
        template_folder=str(ROOT_DIR / "frontend" / "templates"),
        static_folder=str(ROOT_DIR / "frontend" / "static"),
        static_url_path="/static",
    )

    app.config.from_object(Config)

    # Initialize database inside Flask application context
    with app.app_context():
        init_db()

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/about")
    def about():
        return render_template("about.html")

    app.register_blueprint(chat_bp, url_prefix="/api")

    return app
