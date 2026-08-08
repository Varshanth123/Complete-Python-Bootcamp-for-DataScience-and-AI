from flask import Flask, render_template, request  # this render_template is used to render the html file in the flask app

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><body><h1>Welcome to Flask!</h1><p>get and post request</p></body></html>'

@app.route('/index', methods=['GET']) #by default the method is GET, so we can also write it as @app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST']) #this route can handle both GET and POST requests
# GET request is used to retrieve data from the server, 
# while POST request is used to send data to the server
def form():
    if request.method == 'POST': # this block will be executed when the form is submitted
        name = request.form['name']
        return f'<h1>Hello {name}!<br> Your information has been submitted.</h1>' #this will display the name entered in the form
    return render_template('form.html') #this will look for the form.html file in the templates folder and render it


if __name__ == '__main__':
    app.run(debug=True)