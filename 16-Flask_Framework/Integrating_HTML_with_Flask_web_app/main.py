from flask import Flask,render_template #this render_template is used to render the html file in the flask app

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<html><body><h1>Welcome to Flask!</h1></body></html>'

@app.route('/index')
def index():
    return render_template('index.html') 
#this will look for the index.html file in the templates folder and render it
# if it does not find the file it will give an TemplateNotFound error

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)