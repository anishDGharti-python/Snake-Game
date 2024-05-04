

# # slicing
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# # print(piano_keys[2:5])
# # print(piano_keys[2:7:2])
# # print(piano_keys[:5])
# # print(piano_keys[::2]) 
# print(piano_keys[::-1])

from turtle import  Screen, Turtle, Screen


# starting_positions = [(0,0), (-20, 0), (-40,0)]
# screen =Screen()
# screen.setup(width=600, height=600)
# screen.title("snake game")
# screen.bgcolor("black")
# segments = []

# for i in range(0, 3):
#     new_segment  = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(starting_positions[i])

#     segments.append(new_segment)

# for segment_num in range(len(segments)- 1, 0, -1):
#     new_x = segments[segment_num -1].xcor()
#     new_y = segments[segment_num -1].ycor()
#     segments[segment_num].goto(new_x, new_y)


#     segments[segment_num].forward(20)

# screen.exitonclick()
screen = Screen()
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.speed(0)


    def refresh(self):
        random_x =random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    snake.move()

    # detect collision with food using distance method
    if snake.head.distance(food) <10:
        print("eat")