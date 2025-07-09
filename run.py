from flask import Flask
from app.config import Config
from app.models import db
from app.admin.views import admin_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 