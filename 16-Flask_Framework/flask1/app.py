from flask import Flask

# initialize the Flask application
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__) # __name__ is the entry point of the application, and it helps Flask determine the root path of the application.

@app.route('/') # This decorator tells Flask that the function below it should be called when the root URL ("/") is accessed.
def welcome():
    return 'Welcome to Flask!......' # This function returns a simple string that will be displayed in the browser when the root URL is accessed.

@app.route('/hello') # This decorator tells Flask that the function below it should be called when the "/hello" URL is accessed.
def hello():
    return 'Hello, World!......' # This function returns a simple string that will be displayed in the browser when the "/hello" URL is accessed.

if __name__ == '__main__':
    # run the application on the local development server
    app.run(debug=True) # The debug=True argument enables the debugger and automatic reloading of the application when code changes are detected. This is useful during development but should be turned off in production.