from file_conf import FileConf
from flask import Flask
from routes import *

flask_app = Flask(__name__)

file_conf_obj = FileConf('conf.json')

flask_app.register_blueprint(test_page)
flask_app.register_blueprint(stt_page)

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000)