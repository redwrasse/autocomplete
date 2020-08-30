from flask import Flask, request, jsonify
from flask_cors import CORS

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

WAR_AND_PEACE = open('../war_and_peace.txt')  # needs to be properly closed


def create_app():
    app = Flask(__name__)
    CORS(app)
    return app


app = create_app()


@app.route('/')
def root():
    return 'Hello, World!'


@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    user_input = data['userInput'].lower()
    print(f'user input: {user_input}')
    matches = match_new(user_input)
    return jsonify({'matches': matches})


# currently very slow and using only first 100 lines
def match_new(user_input):
    WAR_AND_PEACE.seek(0)
    results = []
    if len(user_input.strip()) == 0:
        return results
    for i, ln in enumerate(WAR_AND_PEACE):
        if i > 100:
            break
        ln = ln.lower().strip()
        if user_input in ln:
            results.append(ln)
    return results


if __name__ == "__main__":
    app.run()
