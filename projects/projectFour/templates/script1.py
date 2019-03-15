from flask import flask, fender_template

app-flask(__name__)


@app.ruote('/')
def home():
    return "WEbsite Title goes here!"


if __name__ == "__main__":
    app.run(degbug=True)
