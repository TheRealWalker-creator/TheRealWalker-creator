import turtle

jarvis = turtle.Screen()
jarvis.title("Jarvis Calculator")
jarvis.bgcolor('black')
jarvis.setup(width=600, height=700)
jarvis.tracer(0)

# Creating the body of the calculator

cal_body = turtle.Turtle()
cal_body.shape('square')
cal_body.shapesize(30, 25)
cal_body.color('#e6e7e8')
cal_body.goto(0, 0)

# Creating the display screen

dis_screen = turtle.Turtle()
dis_screen.shape('square')
dis_screen.shapesize(10, 20)
dis_screen.color('black')
dis_screen.goto(0, 150)

# Pen for performing math problem

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color('yellow')
pen1.penup()
pen1.hideturtle()
pen1.goto(300, 650)
pen1.write("Enter", align="center", font=("courier", 15, "normal"))

# Creating the number buttons
num_button_0 = turtle.Turtle()
num_button_0.shape('square')
num_button_0.shapesize(2.5, 2.5)
num_button_0.color('red')
num_button_0.goto(-170, -30)

num_button_1 = turtle.Turtle()
num_button_1.shape('square')
num_button_1.shapesize(2.5, 2.5)
num_button_1.color('red')
num_button_1.goto(-100, -30)

num_button_2 = turtle.Turtle()
num_button_2.shape('square')
num_button_2.shapesize(2.5, 2.5)
num_button_2.color('red')
num_button_2.goto(-30, -30)

num_button_3 = turtle.Turtle()
num_button_3.shape('square')
num_button_3.shapesize(2.5, 2.5)
num_button_3.color('red')
num_button_3.goto(-170, -100)

num_button_4 = turtle.Turtle()
num_button_4.shape('square')
num_button_4.shapesize(2.5, 2.5)
num_button_4.color('red')
num_button_4.goto(-100, -100)

num_button_5 = turtle.Turtle()
num_button_5.shape('square')
num_button_5.shapesize(2.5, 2.5)
num_button_5.color('red')
num_button_5.goto(-30, -100)

num_button_6 = turtle.Turtle()
num_button_6.shape('square')
num_button_6.shapesize(2.5, 2.5)
num_button_6.color('red')
num_button_6.goto(-170, -170)

num_button_7 = turtle.Turtle()
num_button_7.shape('square')
num_button_7.shapesize(2.5, 2.5)
num_button_7.color('red')
num_button_7.goto(-100, -170)

num_button_8 = turtle.Turtle()
num_button_8.shape('square')
num_button_8.shapesize(2.5, 2.5)
num_button_8.color('red')
num_button_8.goto(-30, -170)

num_button_9 = turtle.Turtle()
num_button_9.shape('square')
num_button_9.shapesize(2.5, 2.5)
num_button_9.color('red')
num_button_9.goto(-170, -240)

# Creating the operator button

add_button = turtle.Turtle()
add_button.shape('square')
add_button.shapesize(9.5, 5)
add_button.color('green')
add_button.goto(65, -100)

sub_button = turtle.Turtle()
sub_button.shape('square')
sub_button.shapesize(2.5, 3.2)
sub_button.color('black')
sub_button.goto(169, -30)

mult_button = turtle.Turtle()
mult_button.shape('square')
mult_button.shapesize(2.5, 3.2)
mult_button.color('red')
mult_button.goto(169, -100)

div_button = turtle.Turtle()
div_button.shape('square')
div_button.shapesize(2.5, 3.2)
div_button.color('blue')
div_button.goto(169, -170)


while True:
    jarvis.update()
