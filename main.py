from flask import Flask
from application.database import *
from flask_restful import Api
from flask_cors import CORS


app = None
api = None
Base_url = 'http://127.0.0.1:5000'

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(LocalDevelopmentConfig)
    app.config['SECRET_KEY'] = 'Vish30'
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    CORS(app)

    return app, api


app, api = create_app()


from application.controllers import *
from application.api import *









if __name__ == '__main__':
    app.run(debug=True)