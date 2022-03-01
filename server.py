from flask import Flask

app = Flask(__name__)

@app.route("/")
def status():
    return "{ Online }"

@app.route("/test")
def test():
    print("hello on the terminal")
    return "Check the terminal dumb ass"