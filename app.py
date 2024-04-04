from flask import Flask, request, jsonify
from model import compute_similarity

app = Flask(__name__)


@app.route("/similarity", methods=["POST"])
def similarity():
    data = request.get_json()
    text1 = data["text1"]
    text2 = data["text2"]
    score = compute_similarity(text1, text2)
    return jsonify({"similarity score": score})


if __name__ == "__main__":
    app.run(debug=True)
