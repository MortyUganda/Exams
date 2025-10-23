import turtle

def rectangle(width, height):
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(width)
            turtle.left(90)
        else:
            turtle.forward(height)
            turtle.left(90)
        
width = 190
height = 90
rectangle(width, height)