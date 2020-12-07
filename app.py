from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return "Penguins are cute!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite desert."""
    return f'How did you know I liked {users_dessert} ?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a message to the user that changes based on their noun and adjective."""
    return f'{noun} has no {adjective} in the car'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() == False or number2.isdigit() == False:
        return f'invalid inputs. Please try again by entering 2 numbers!'
    else:
        answer = int(number1) * int(number2)
        return f'You multiplied {number1} and {number2} to get {answer}.'


if __name__ == '__main__':
    app.run(debug=True)