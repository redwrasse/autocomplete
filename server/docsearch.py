from flask import Flask, request, jsonify
from flask_cors import CORS
import autocomplete
import time
#
# OPTIONS = [
#     "Apple",
#     "Papaya",
#     "Persimmon",
#     "Paw Paw",
#     "Prickly Pear",
#     "Peach",
#     "Pomegranate",
#     "Pineapple"
# ]


def create_app():
    app = Flask(__name__)
    CORS(app)
    return app


app = create_app()
ac = autocomplete.Autocomplete3()


@app.route('/')
def root():
    return 'Hello, World!'


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data['userInput'].lower()
    start = time.time()
    print(f'user input: {user_input}')
    matches = ac.match(user_input)
    end = time.time()
    diff = end - start
    print(f'search time: {diff}')
    return jsonify({'matches': matches})


if __name__ == "__main__":
    app.run()
