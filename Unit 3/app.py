from typing import Text
from flask import Flask, render_template

app = Flask(__name__ , template_folder='templates')

@app.route("/")
def start():
    title = "Forest"

    picture = "https://images.fineartamerica.com/images-medium-large-5/snow-flakes-against-the-dark-forest-blake-jorgenson.jpg"

    text = """Snowflakes fell from the dark, chilly sky. You stumble upon a dark forest. Suddenly you hear a loud howl from the forest!
      """
      
    choices = [
        ('enter_forest',"Enter forest"),
        ('run_away',"Turn around and run!")

    ]  
    return render_template('adventures.html', title=title , text=text , choices=choices, picture_url = picture) 


@app.route("/inside")
def enter_forest():
    title = "You entered the forest..."

    picture = "https://t4.ftcdn.net/jpg/03/21/60/71/360_F_321607144_e0dnqrWJYkg8HNSfehxTFwFGJpKvalu5.jpg"

    text = """ ... there is not much to see at first, only snow and trees. You come across a sign, but can`t clearly tell what it says. You clean it up, and realize it says DANGER. You need to decide to go ahead or not."""

    choices = [
        ('go_ahead', "Continue"),
        ('run_away', "Turn around and run")
    ]
    return render_template('adventures.html', title=title , text=text , choices=choices, picture_url = picture) 



@app.route("/escape")
def run_away():
    title = "You run away!"

    picture = "https://p0.pikist.com/photos/641/867/nature-landscape-mountain-woods-forest-snow-winter-cold-weather.jpg"

    text = """ You turn around and run as fast as you can! You hear one more howl, louder than the last one. """

    choices = []

    return render_template('adventures.html', title=title , text=text , choices=choices, picture_url = picture) 


@app.route("/continue")
def go_ahead():
    title = "Look out!"

    picture = "https://ak.picdn.net/shutterstock/videos/1019888506/thumb/1.jpg"

    text = """" As you continue walking, you start seeing blood all around you in the snow. You look up and see a big wolf. You look into his eyes, and that is the last thing you see."""

    choices = []

    return render_template('adventures.html', title=title , text=text , choices=choices, picture_url = picture) 

