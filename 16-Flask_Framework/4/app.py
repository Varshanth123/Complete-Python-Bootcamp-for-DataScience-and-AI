from flask import Flask, render_template,request  # this render_template is used to render the html file in the flask app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST']) 
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    name = request.form['name']
    return f'<h1>Hello {name}!<br> Your information has been submitted.</h1>'

if __name__ == '__main__':
    app.run(debug=True)