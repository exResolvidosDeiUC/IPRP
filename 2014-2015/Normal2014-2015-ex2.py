import turtle
import random
def circulo1(raio,raio_menor,pos_x,pos_y):
    for i in range(2):
        turtle.penup()
        turtle.goto(pos_x,pos_y)
        turtle.pendown()
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(raio)
        turtle.end_fill()
        pos_y = pos_y+25
        raio=raio-25
        turtle.goto(pos_x,pos_y)
        turtle.pendown()
        turtle.fillcolor('white')
        turtle.begin_fill()
        turtle.circle(raio)
        turtle.end_fill() 
        pos_y = pos_y+25
        raio=raio-25
    turtle.penup()
    turtle.setposition(random.randint(-100+raio_menor,100-raio_menor),random.randint(0,200-(2*raio_menor)))
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(raio_menor)
    turtle.end_fill()
circulo1(100,10,0,0)
turtle.hideturtle()
turtle.exitonclick()