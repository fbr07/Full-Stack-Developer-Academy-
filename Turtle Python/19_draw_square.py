import turtle
jack = turtle.Turtle()
jack.color("yellow")

def draw_square(length, color):
    for side in range(4):
        jack.color(color)
        jack.forward(length)
        jack.right(90)

draw_square(100, "cyan")
draw_square(50, "magenta")
draw_square(25, "yellow")

import turtle

# Write a function here that creates a
# turtle and draws a shape with it.
def triangle_boogie(color, start):
  t = turtle.Turtle()
  t.color(color)
  t.speed(0)
  t.width(5)
  t.right(start)
  for shape in range(6):
    for side in range(3):
      t.forward(100)
      t.right(120)
    t.right(15)
  t.hideturtle()

# Call the function multiple times.
triangle_boogie("red", 0)
triangle_boogie("orange", 120)
triangle_boogie("blue", 240)