"""Greeting Flask app."""

from random import choice

from flask import Flask, request, render_template

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return render_template('homepage.html')


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return render_template('hello.html')

@app.route('/compliment')
def get_comp():
  
  return render_template('compliment.html')

@app.route('/diss')
def get_diss():
  
  return render_template('diss.html')


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get('person')

    greeting = request.args.get('greeting')
    # compliment = choice(AWESOMENESS)

    return render_template('greet.html')


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
