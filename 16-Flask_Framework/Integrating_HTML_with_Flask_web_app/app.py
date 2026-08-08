from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><body><h1>Welcome to Flask app!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True)