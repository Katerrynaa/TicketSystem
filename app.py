from flask import Flask

from src.models import db_connect, db_disconnect
from src.config import read_config, read_key_config
from src.views import auth
from src.managers import login_manager


app = Flask(__name__)

login_manager.init_app(app)

config = read_config()
app.secret_key = read_key_config().SECRET_KEY


@app.before_request
def before_request():
    db_connect(config.DATABASE_URL)


@app.after_request
def after_request(response):
    db_disconnect()
    return response

app.register_blueprint(auth)  

if __name__ == "__main__":
    app.run(debug=True)
