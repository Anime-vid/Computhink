import turtle
# def DiceGuess(Guess):
#     global ans
#     import random
#     ans = 0
#     ans = random.randint(1,6)
#     if Guess == ans:
#         return True
#     else:
#         return False

BOARD_SIZE = 600
CELL_SIZE = BOARD_SIZE / 3
inbetween = 0
xxcorr = 0
yycorr = 0
def setup_screen():
    window = turtle.Screen()
    window.setworldcoordinates(0,0,BOARD_SIZE, BOARD_SIZE)
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.hideturtle()
    return window,pen
def drawTTT():
    for i in range(1,3):
        pen.penup()
        pen.goto(CELL_SIZE * i,0)
        pen.pendown()
        pen.goto(CELL_SIZE*i,BOARD_SIZE)
        pen.penup()
        pen.goto(0,CELL_SIZE * i)
        pen.pendown()
        pen.goto(BOARD_SIZE,CELL_SIZE*i)
        pen.penup()

window,pen = setup_screen()
drawTTT()
window.mainloop()
