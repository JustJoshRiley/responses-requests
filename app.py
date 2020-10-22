from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return "penguins are cute!"

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
    
    
    if number1.isdigit()  == True and number2.isdigit() == True:
        number_1 = int(number1)
        number_2 = int(number2)
        answer = number_2 * number_1
        return f'{answer}'
    return "Invalid inputs. Please try again by entering 2 numbers!"


if __name__ == '__main__':
    app.run(debug=True)