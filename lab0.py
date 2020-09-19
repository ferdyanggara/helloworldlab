import turtle
import random

# code for drawing with turtle
##turtle.write("Hello World!") # writing with turtle
##turtle.up() # raise the pen up
##turtle.goto(-100,50) # go to the position (-100, 50)
##turtle.down() # put the pen down
##turtle.goto(-100,-50) # go to the position (-100, -50)
##turtle.goto(100,-50) # go to the position (100, -50)
##turtle.goto(100,50) # go to the position (100, 50)
##turtle.goto(-100,50) # go to the position (100, 50)
##turtle.done()




random_width = random.randint( -300 , 300 )
##random_height = random.randint( -300 , 300 )
##turtle.color( "blue", "red" )
##
##turtle.begin_fill()
##turtle.forward( random_width )
##turtle.left(90)
##turtle.forward( random_height )
##turtle.left(90)
##turtle.forward( random_width )
##turtle.left(90)
##turtle.forward( random_height )
##turtle.left(90)
##turtle.end_fill()

turtle.speed(8)
num_of_loops = 0
colors = ["Royal Blue", "Pale Green", "Gold", "Rosy Brown", "Coral", "Orchid"]
random_color = random.choice(colors)
turtle.color("blue", random_color)

turtle.begin_fill()
while num_of_loops < 5: 
    
    turtle.circle( random_width )
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    num_of_loops = num_of_loops + 1

turtle.end_fill()
turtle.done()
##turtle.exitonclick()

