
# userInput = input("What has to be broken before you can use it?")
# is_Correct = False
# word = userInput.split()
# for i in word:
#     if i == "egg":
#         is_Correct = True
#     else:
#         is_Correct = False
# if is_Correct:
#     print("Well done")
# else:
#     print("NOT WELL DONE")
import turtle
window = turtle.Screen()
window.setup(width=600,height=600)
window.bgcolor("lightblue")
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("orange")
t.speed(10000000000000000000000000000000)
t.shape('circle')
# oneone = 360 / 5

# for i in range(0,360,int(360 / 5)):
#     t.seth(i)
#     t.forward(100)
# t.left(5)
size2 = 0
# siz3 = 0
t.goto(0,0)
def abuse(SIDES,size=50):
    global size2
    for i in range(SIDES):
        size2 = size
        t.pendown()
        t.forward(size)
        t.right(360/SIDES)
        t.penup()
def abuse2(SIDES,size=50):
    global size2
    for i in range(SIDES):
        size2 = size
        t.pendown()
        t.forward(size)
        t.left(360/SIDES)
        t.penup()
# for i in range(0,7):
#     abuse(4,50)
#     t.forward(size2 + 10)
# for i in range(0,6):
#     t.backward(size2 + 10)
# siz3 -= size2 + 10
# t.goto(t.xcor(),siz3)
# for i in range(0,4):
#     abuse(4,50)
#     t.forward(size2 + 10)
# for i in range(0,3):
#     t.backward(size2 + 10)
# siz3 -= size2 + 10
# t.goto(t.xcor(),siz3)
# for i in range(0,2):
#     abuse(4,50)
#     t.forward(size2 + 10)
x_loc = 0
y_loc = 0



# def drawsq():
#     print("Hi")
# for i in range(0,7):
#     t.goto(x_loc - (i*50/2),y_loc + (i*50/2))
#     abuse(8,50 + i*50)
abuse(4,50)
abuse2(3,50)

window.mainloop()

















