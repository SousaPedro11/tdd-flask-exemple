from flask import Flask

from app.algoritmos import algoritmos_bp
from app.apresentacao import apresentacao_bp


def create_app(config_name: str = None) -> Flask:
    app = Flask(__name__)

    app.register_blueprint(algoritmos_bp)
    app.register_blueprint(apresentacao_bp)

    return app
