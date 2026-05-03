# print("Hello from lesson 9")
# Even = False
# def isEven(num):
#     global Even
#     if num % 2 == 0:
#         Even = True
#     else:
#         Even = False
# list_num = [3,9,2]
# for i in range(len(list_num)):
#     if isEven(list_num[i]):
#         print(str(list_num[i]) + " is a even number.")
#     else:
#         print(str(list_num[i]) + " is a odd number.")
## Task 2: Age Group
# Create a function that will take in someone’s age and return either of the following based on the age provided:
# - ‘Child’ (Below 13)
# - ‘Teen’ (14-20)
# - ‘Adult’ (21-64), or
# - ‘Senior’ (65 and above)
# def AgeGroup(Age):
#     if Age <= 13:
#         return "Child"
#     if Age >= 14 and Age <= 20:
#         return "Teen"
#     if Age >= 21 and Age <=64:
#         return "Adult"
#     else:
#         return "Senior"
# print(AgeGroup(input("What is your age?")))
# def QW(QWERTY):
#     return QWERTY * 4
# def SQ(SQQ):
#     return SQQ * SQQ
# def SOSQ(SOS,SOSS):
#     return SQ(SOS) + SQ(SOSS)
# print(SOSQ(2,3))
import turtle
def setup_screen(ScreenH,ScreenW):
    window = turtle.Screen()
    window.setup(ScreenW,ScreenH)
    return window
dx = 2
dy = 2
def BB():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("Blue")
    ball.penup()
    return ball
def moveBall(ball,dx,dy):
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)
def cchekx():
    if ball.xcor() > (500/2) or ball.xcor() < (-500/2):
        return True
def ccheky():
    if ball.ycor() > (300/2) or ball.ycor() < (-300/2):
        return True
window = setup_screen(300,500)
ball = BB()
while True:
    moveBall(ball,dx,dy)
    if cchekx():
        dx *= -1
    if ccheky():
        dy *= -1
window.mainloop()

