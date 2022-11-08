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