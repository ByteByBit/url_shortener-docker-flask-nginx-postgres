from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    ''' Create Flask app. '''

    app = Flask(__name__)

    app.config.from_object('project.config.Config')
    db.init_app(app)
    with app.app_context():

        # Register blueprint.
        from project.routes import shortener_bp
        app.register_blueprint(shortener_bp)

        # DB initialized at the router service.

        return app
