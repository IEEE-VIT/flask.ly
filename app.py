from flask import Flask
from routes.routes import router
from models import db
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.sqlite3' 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "sqlite:///app.db"
    db.init_app(app)
    return app

app=create_app()





app.register_blueprint(router);

if __name__=='__main__':
    db.create_all(app=create_app())
    app.run(debug=True)
