from flask import jsonify, Blueprint

test_page = Blueprint('test_page', __name__, template_folder='templates')
@test_page.route('/', methods=['GET'])
def test():
    return jsonify(msg=f"hello world!")