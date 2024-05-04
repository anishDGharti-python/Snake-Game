from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen =Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard= ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # detect collision with food using distance method
    if snake.head.distance(food) < 15:
           # print('detect')
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall         ss
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        
    # detect collision with tail:  
    # if head collides with any of the segments of the snake then game over
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over() 
            scoreboard.reset()
            snake.reset()

   
        

screen.exitonclick()