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
        from project.routes import route_bp
        app.register_blueprint(route_bp)

        # Set up DB.
        db.create_all()
        from project.models import URI_Table

        if not URI_Table.is_initialized():
            # Insert first row to avoid upcoming headaches.
            db.session.add(URI_Table(url="https://google.com", s_url='a', index=0))

        db.session.commit()

        return app
