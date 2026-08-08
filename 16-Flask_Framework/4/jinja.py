# Building url Dynamically
# variable rule
# Jinja 2 Template engine (is used to build urls dynamically in Flask. The url_for() function is used to build urls dynamically. It takes the name of the view function as the first argument and any number of keyword arguments corresponding to the variable parts of the url rule as the second argument.)

# Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''
from flask import Flask, render_template,request,redirect,url_for  # this render_template is used to render the html file in the flask app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST']) 
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    name = request.form['name']
    return f'<h1>Hello {name}!<br> Your information has been submitted.</h1>'

# Variable rule
@app.route('/success/<username>') # This route expects a variable part called 'username'
def success(username):
    return f'hey {username} you have successfully logged in!'

@app.route('/score/<float:score>') # This route expects a variable part called 'score' which is an integer
def score(score):
    res=''
    if score >= 50:
        res='PASSED'
    else:
        res='FAILED'
    return render_template('result.html', result=res, marks=score)

@app.route('/successres/<int:score>') # This route expects a variable part called 'score' which is an integer
def successres(score):
    res=''
    if score >= 50:
        res='PASSED'
    else:
        res='FAILED'
    exp={'score':score,'res':res}
    return render_template('result1.html', results=exp)

@app.route('/ifcondition/<int:score>')
def ifcondition(score):
    return render_template('result2.html',marks=score)

# Building url Dynamically
@app.route('/marks')
def marks():
    return render_template('getresult.html')

@app.route('/getresult',methods=['GET','POST'])
def getresult():
    total=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total=(science+c+maths+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('score',score=total))

if __name__ == '__main__':
    app.run(debug=True)
