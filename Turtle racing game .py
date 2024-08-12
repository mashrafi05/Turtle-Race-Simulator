import turtle
from turtle import Turtle, Screen
import random

race_on=False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors=["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtle = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race_on=True

while race_on:


    for turtle in all_turtle:
        if turtle.xcor()>230:
            race_on= False
            winning_colour=turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")


        random_distace= random.randint(1,10)
        turtle.forward(random_distace)


screen.exitonclick()
