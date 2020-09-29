from flask import Flask
from routes import router

app=Flask(__name__)

app.register_blueprint(router);


if __name__=='__main__':
    app.run()
