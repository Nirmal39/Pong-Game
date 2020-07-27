import turtle
import os
import time

wn=turtle.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.title("pong")
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#FUNCTIONS
#paddle_a_up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=30
    paddle_a.sety(y)
#paddle_b_up
def paddle_b_up():
    y=paddle_b.ycor()
    y+=30
    paddle_b.sety(y)
#paddle_a_down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=30
    paddle_b.sety(y)
#paddle_a_down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=30
    paddle_a.sety(y)

#keyboard bindings

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main loop

while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #check border
    #up and down
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        #os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        #os.system("afplay bounce.wav&")

    #left and right
    if ball.xcor() > 350:
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1

    elif ball.xcor() < -350:
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1       

    #ball and paddle collisions

    if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor()+50 and ball.ycor()  > paddle_b.ycor()-50 :
        ball.dx*=-1
        #os.system("afplay bounce.wav&")

    elif ball.xcor() < -340 and ball.ycor() < paddle_a.ycor()+50 and ball.ycor()  > paddle_a.ycor()-50 :
        ball.dx*=-1
        #os.system("afplay bounce.wav&")            

    
    if score_a==10:
        wn.clear()
        wn.bgcolor("black")
        pen.goto(0,0)
        pen.write(" Game over\nplayer B won",align="center", font=("Courier", 32, "normal"))
        time.sleep(5)
        break
    elif score_b==10:
        wn.clear()
        wn.bgcolor("black")
        pen.goto(0,0)
        pen.write(" Game over\nplayer B won",align="center", font=("Courier", 32, "normal"))
        time.sleep(5)
        break