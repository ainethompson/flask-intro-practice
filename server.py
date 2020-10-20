"""Greeting Flask app."""

from random import choice

from flask import Flask, request

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

    return """
    <!doctype html>
    <html>
      <a href="/hello">Start here</a>
        Hi! This is the home page.
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action='/greeting'>
          What's your name?
          <input type='text' name='person' required>
        </form>
        
        <form action='/compliment'>
          Would you like a compliment?
          <input type='submit' value='Compliment'>
        </form>

        <form action='/diss'>
          ... Or would you prefer an insult?
          <input type='submit' value='Insult'>
        </form>
      </body>
    </html>
"""
        # <form action='/compliment-insult'>
        #   What's your name? <input type="text" name="person">
        #   Would you like a compliment or an insult?
        #   <input type='button' value='Compliment'>
        #   <input type='button' value='Insult'>
        #   <input type='submit' value=Submit>
        # </form>


 

   
@app.route('/compliment')
def get_comp():
  
  return """
  <!doctype html>
  <html>
  <body>
    <h1>Choose a compliment</h1>
    <form action='/greet'>
      What compliment would you like?
      <select name="greeting"
        <option value="awesome">Awesome</option>
        <option value="terrific">Terrific</option>
        <option value="fantastic">Fantastic</option>
        <option value="neato">Neato</option>
        <option value="fantabulous">Fantabulous</option>
        <option value="wowza">Wowza</option>
      </select>
      <input type="submit" value="Submit">
    </form>
  </body>
  </html>
  """

@app.route('/diss')
def get_diss():
  
  return """
  <!doctype html>
  <html>
  <body>
   <h1>Choose an insult</h1>
    <form action='/greet'>
      What insult would you like?
      <select name="greeting">
        <option value='ugly'>Ugly</option>
        <option value='stupid'>Stupid</option>
        <option value='selfish'>Selfish</option>
        <option value='lazy'>Lazy</option>
        <option value='broke'>Broke</option>
        <option value='rude'>Rude</option>
      </select>
      <input type='submit' value='Submit'>
    </form>
  </body>
  </html>
  """
@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    greeting = request.args.get("greeting")
    # compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <body>
        Hi, {player}! I think you're {greeting}!
      </body>
    </html>
    """
    # .format(player, greeting)


# @app.route('/diss')
# def diss_person():
#   """ let user choose diss """
#   return """
#   <!doctype html>
#   <html>
#     <head> 
#       <title>A Diss</title>
#     </head>
#     <body>
#       Hi, {player}! I think you're {insult}!
#     </body>
#   </html>
#   """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
