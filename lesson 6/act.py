import turtle
turtle.Screen().bgcolor("pink")
sc=turtle.Screen()
sc.setup(400,300)
turtle.title("Welcome to turtle world!")
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i=i+1
turtle.done()