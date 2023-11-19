#Example 38 - Spiral
import turtle



t = turtle.Turtle()
t.speed("slow")
t.pensize(3)
t.pencolor("blue")

colors = ("red", "blue", "green", "purple")

num_sides = 4 

for x in range(360):
    t.pencolor(colors[x % len(colors)])
    t.forward(x)
    t.left(360/num_sides + 2)



