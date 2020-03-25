from flask import jsonify, Blueprint, render_template

stt_page = Blueprint('stt_page', __name__, template_folder='../templates')
@stt_page.route('/stt', methods=['GET'])
def test():
    return render_template('STT_demo.html')