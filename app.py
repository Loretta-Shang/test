from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    env = os.getenv('ENV', 'dev')  # Default to 'dev' if ENV is not set
    if env == 'prod':
        return "hello prod"
    else:
        return "hello dev"

if __name__ == '__main__':
    app.run(debug=True)
