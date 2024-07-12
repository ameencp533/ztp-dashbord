from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    Bootstrap(app)
    
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
        db.create_all()
        
        return app
