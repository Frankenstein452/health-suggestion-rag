from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health-advice', methods=['GET'])
def health_advice():
    advice = {
        "advice": "Stay hydrated, eat a balanced diet, and exercise regularly."
    }
    return jsonify(advice)

if __name__ == '__main__':
    app.run(debug=True)