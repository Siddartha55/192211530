from flask import Flask, jsonify
from collections import deque

app = Flask(__name__)
app.app_context().push()

WINDOW_SIZE = 10
window = deque(maxlen=WINDOW_SIZE)

NUMBER_SETS = {
    'p': [2, 3, 5, 7, 11, 13],
    'f': [0, 1, 1, 2, 3, 5, 8, 13],
    'e': [2, 4, 6, 8, 10, 12],
    'r': [9, 14, 7, 3, 11, 6]
}

API_URLS = {
    'p': 'http://127.0.0.1:9876/numbers/p',
    'f': 'http://127.0.0.1:9876/numbers/f',
    'e': 'http://127.0.0.1:9876/numbers/e',
    'r': 'http://127.0.0.1:9876/numbers/r'
}

@app.route('/numbers/<string:number_id>', methods=['GET'])
def get_numbers(number_id):
    if number_id not in NUMBER_SETS:
        return jsonify({'error': 'Invalid number ID'}), 400

    numbers = [6,8,10,12,14,16,18,20,22,24,26,28,30]

    prev_state = list(window)

    for num in numbers:
        if num not in window:
            window.append(num)

    curr_state = list(window)
    avg = round(sum(curr_state) / len(curr_state), 2) if curr_state else 0

    return jsonify({
        "windowPrevState": prev_state,
        "windowCurrState": curr_state,
        "numbers": numbers,
        "avg": avg
    })

@app.route('/')
def index():
    return "Server is running successfully on port 9876!"

if __name__ == '__main__':
    app.run(debug=True, port=9876)
