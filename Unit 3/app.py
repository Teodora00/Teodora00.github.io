from typing import Text
from flask import Flask, render_template

app = Flask(__name__ , template_folder='templates')

@app.route("/")
def start():
    title = "Forest"

    text = """Snowflakes fell from the dark, chilly sky. You stumble upon a dark forest. Suddenly you hear a loud howl from the forest!
      """
      
    choices = [
        ('enter_forest',"Enter forest"),
        ('run_away',"Turn around and run!")

    ]  
    return render_template('adventures.html', title=title , text=text , choices=choices) 


@app.route("/inside")
def enter_forest():
    title = "You entered the forest..."

    text = """ ... there is not much to see at first, only snow and trees. You come across a sign, but can`t clearly tell what it says. You clean it up, and realize it says DANGER. You need to decide to go ahead or not."""

    choices = [
        ('go_ahead', "Continue"),
        ('run_away', "Turn around and run")
    ]
    return render_template('adventures.html', title=title , text=text , choices=choices) 


@app.route("/escape")
def run_away():
    title = "You run away!"

    text = """ You turn around and run as fast as you can! You hear one more howl, louder than the last one. """

    choices = []

    return render_template('adventures.html', title=title , text=text , choices=choices) 

@app.route("/continue")
def go_ahead():
    title = "Look out!"

    text = """" As you continue walking, you start seeing blood all around you in the snow. You look up and see a big wolf. You look into his eyes, and that is the last thing you see."""

    choices = []

    return render_template('adventures.html', title=title, text=text, choices=choices)
