from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]
turtle_gang = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_gang.append(new_turtle)

if user_bet:
    game_on = True
while game_on:
    for turtle in turtle_gang:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won!, The {winning_color} was the winning turtle.")
            else:
                print(f"You lost!, The {winning_color} turtle won the race.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()