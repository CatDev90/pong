import turtle


#Settign up the wnidow
window = turtle.Screen()
window.title('I thought this was tetris')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer()


# Score
scoreA = 0
scoreB = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = -6

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write(f'Player A: 0 Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Functions
'''
Paddle A (The left paddle)
'''
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

'''
Paddle B (The right paddle)
'''
def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    window.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
   
    # Ball Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        scoreB += 1
        pen.write(f'Player A: {scoreA} Player B: {scoreB}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f'Player A: {scoreA} Player B: {scoreB}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

    # Paddle and ball collisions 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
