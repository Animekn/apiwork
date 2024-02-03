from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')#http:localhost:5000/
def home():
    return "Hello, World!"

@app.route('/blog')#http:localhost:5000/blog
def blog():
    return "Hello, World! welcome to my blog"

app.run(port=5000, debug=True)
