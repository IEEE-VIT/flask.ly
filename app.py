from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.routes import router


app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(router)
db = SQLAlchemy(app)


def db_init():
    from models import Url, User
    db.create_all()
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    db_init()
    app.run()
