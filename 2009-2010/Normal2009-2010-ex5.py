import turtle

def triangulo_inc(lado, ang):
    turtle.setheading(ang)
    for i in [lado, lado+lado/10, lado+lado/5]:
        turtle.forward(i)
        turtle.right(120)
        
def desenho(lado):
    for i in range(10):
        triangulo_inc(lado-20*i, 0 - 5 * i)  
    turtle.hideturtle()
    turtle.exitonclick()    

if __name__ == '__main__':
    desenho(400)
    