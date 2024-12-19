
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate-habit-suggestions', methods=['GET'])
def generate_habit_suggestions():
    suggestions = [
        {"title": "Drink Water", "description": "Stay hydrated by drinking 8 glasses of water daily."},
        {"title": "Morning Stretch", "description": "Start your day with a 5-minute stretching session."},
        {"title": "Read a Book", "description": "Develop your mind by reading at least 20 pages daily."}
    ]
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(debug=True)
