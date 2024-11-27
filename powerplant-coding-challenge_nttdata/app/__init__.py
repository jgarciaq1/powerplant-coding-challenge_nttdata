from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registrar rutas
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
