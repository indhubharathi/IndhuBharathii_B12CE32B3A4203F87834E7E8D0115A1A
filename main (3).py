"""'''Implement a class called Player that represent a cricket player.        The Player class; should have a 
method called play() which prints "The player is playing cricket.          Derive two classes, Batsman and
Bowler, from the player class. Override the play() method in each          derrived class to print "The batsman
is batting" and "The bowlerr is bowling", respectively. Write a            program to create objects of both the
Batsman and Bowler classes and call the play() method for each             object.'''


# Define the base clas player
class Player:
    def Play(self):
      print("The player is playing cricket.")

# Define the derived class batsman
class Batsman(Player):
    def play(self):
      print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
         print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play( method for each object
batsman.play()
bowler.play()
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(75)
    t.left(90)