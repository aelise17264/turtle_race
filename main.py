from turtle import Turtle, Screen
import random

race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-160, -100, -40, 20, 80, 140]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You loose. The {winning_color} turtle is the winner")

        ran_dist = random.randint(0, 10)
        turtle.forward(ran_dist)


my_screen.exitonclick()