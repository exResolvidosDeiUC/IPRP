import math
import turtle
def triangulos(n, base, lado):
    #x0 = -base/2
    #x1 = base/2
    #y0 = y1 = sqrt((base/2)^2 + lado^2)
    x = -base/2
    y = -math.sqrt((base/2)**2 + lado**2)
    #x e y são coordenadas do canto inferior esquerdo do triangulo maior
    for i in range(n):
        turtle.setheading(turtle.towards(x, y)) #aponta na direcao do canto inferior esquerdo
        turtle.forward((i+1)*lado) #avanca o comprimento de n (i+1) lados sendo n o numero do triangulo a desenhar atualmente
        turtle.goto(-turtle.position()[0],turtle.position()[1]) #vai para a posicao simetrica ao canto inferior esquerdo (canto inferior direito)
        turtle.goto(0,0) #volta à origem, canto superior
    turtle.hideturtle()
    turtle.exitonclick()
triangulos(5, 100, 20)
