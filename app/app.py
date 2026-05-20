# app/app.py
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    xff = request.headers.get('X-Forwarded-For', 'Not present')
    return f"""
    <h2>X-Forwarded-For header:</h2>
    <pre>{xff}</pre>
    <h3>Full headers:</h3>
    <pre>{dict(request.headers)}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
