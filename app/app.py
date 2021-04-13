from flask import Flask, request, jsonify
from flask_cors import CORS
import shard


def create_app():
    app = Flask(__name__)
    CORS(app)  # !! CORS for development only
    return app


app = create_app()
ac_shard = shard.Shard(start='a', end='z')


@app.route('/health')
def root():
    return 'Health check'


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data['userInput']
    matches = ac_shard.match(user_input)
    return jsonify({'matches': matches})
