from flask import Flask
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random():
    return f"Random number: {random.randint(1, 100)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
