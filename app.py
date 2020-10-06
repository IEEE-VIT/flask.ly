from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.routes import router


app = Flask(__name__)
app.config.from_object('settings')
app.register_blueprint(router)
db = SQLAlchemy(app)


@app.before_first_request
def db_init():
    db.create_all()


if __name__ == '__main__':
    app.run()
