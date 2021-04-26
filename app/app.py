from flask import Flask, request, jsonify
from flask_cors import CORS
import shard
import os


def create_app():
    app = Flask(__name__)
    CORS(app)  # !! CORS for development only
    return app


app = create_app()
prefix_range = os.environ['PREFIX_RANGE']
start, end = prefix_range.split('-')
print(f'building shard {start}-{end} ...')
ac_shard = shard.Shard(start=start,
                       end=end)


@app.route('/health')
def root():
    return 'Health check'


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data['userInput']
    matches = ac_shard.match(user_input)
    return jsonify({'matches': matches})
