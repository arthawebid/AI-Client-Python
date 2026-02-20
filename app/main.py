from flask import Flask, request, jsonify
import logging
from .ai_client import ask_ai
from .config import Config

def create_app():
    app = Flask(__name__)

    logging.basicConfig(
        filename="logs/app.log",
        level=getattr(logging, Config.LOG_LEVEL),
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})

    @app.route("/ask", methods=["POST"])
    def ask():
        data = request.json
        prompt = data.get("prompt", "")
        model = data.get("model", "flash")

        result = ask_ai(prompt, model)
        return jsonify(result)

    return app