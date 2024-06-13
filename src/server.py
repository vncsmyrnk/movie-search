import os
from flask import Flask
from flask_cors import CORS
from routes import build_query_routes


def build_app():
    app = Flask(__name__)
    bp_search = build_query_routes()

    cors_resources = {
        r"/api/*": {
            "origins": [
                "http://localhost:3000",
                "https://stephany-c.github.io",
            ],
            "allow_headers": "*",
            "expose_headers": "*",
        }
    }

    CORS(app, resources=cors_resources, supports_credentials=True)

    with app.app_context():
        app.register_blueprint(bp_search, url_prefix="/api/query")

    @app.route("/api")
    def display_app_data():
        return {
            "name": "Movie Search API",
            "version": os.getenv("APP_VERSION", "v0.0.0"),
        }

    return app


app = build_app()
