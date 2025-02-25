from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_dotenv import DotEnv
from config import Config
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
env = DotEnv()

def create_app(config_class=Config):
    app = Flask(__name__)

    # Load environment variables
    env.init_app(app)

    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register blueprints
    from app.routes import faq_routes, auth_routes, event_routes
    app.register_blueprint(faq_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(event_routes.bp)

    return app