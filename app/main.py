from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() # take env vars from .env

app = Flask(__name__)

@app.route('/<random-string>')
def return_backwards_string(random_string):
    return "".join(reverse(random_string))

@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    