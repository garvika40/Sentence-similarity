from flask import Flask, request, jsonify
from model import similarity

app = Flask(__name__)

@app.route('/')
def redirect_msg():
    return 'Send post req to /similarity'

@app.route('/test', methods=['POST'])
def test():
    return jsonify({"similarity score": 0.5})

@app.route('/similarity', methods=['POST'])
def similarity_handler():
    data = request.get_json(force=True)
    text1 = data.get('text1')
    text2 = data.get('text2')
    score = similarity(text1, text2);
    return jsonify({"similarity score": score})
