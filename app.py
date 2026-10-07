from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Het werkt! Flask draait in PyCharm."

if __name__ == "__main__":
    app.run(debug=True)
