from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    frontend_url = getenv("FRONTEND_URL", "*")  # default * if not set
    CORS(app)


    from app.routes.score import bp as score_bp
    from app.routes.history import bp as history_bp
    from app.routes.summary import bp as summary_bp
    
    app.register_blueprint(score_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(summary_bp)

    return app