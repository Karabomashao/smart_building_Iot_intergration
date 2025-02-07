from flask import Flask

app = Flask(__name__)

@app.route("/")
def test_flask():
    # print()
    return "Testing if it works."


if __name__ == "__main__":
    app.run(debug=True, port=5000)