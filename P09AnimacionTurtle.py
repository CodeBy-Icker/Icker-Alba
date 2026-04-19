#Icker Alba
import turtle
 
# Configuración
pantalla = turtle.Screen()
pantalla.title("Animación - Pelota Rebotando")
pantalla.bgcolor("#1a1a2e")
pantalla.setup(width=600, height=400)
pantalla.tracer(0)
 
# Pelota
pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("cyan")
pelota.penup()
pelota.goto(0, 0)
 
# Movimiento
dx = 3
dy = 3
 
# Marcador
marcador = turtle.Turtle()
marcador.hideturtle()
marcador.penup()
marcador.goto(0, 160)
marcador.color("white")
rebotes = 0
 
while True:
    pantalla.update()
 
    # Mover
    x = pelota.xcor() + dx
    y = pelota.ycor() + dy
    pelota.goto(x, y)
 
    # Rebote en paredes
    if pelota.xcor() > 280 or pelota.xcor() < -280:
        dx *= -1
        rebotes += 1
 
    if pelota.ycor() > 180 or pelota.ycor() < -180:
        dy *= -1
        rebotes += 1
 
    # Actualizar marcador
    marcador.clear()
    marcador.write(f"Rebotes: {rebotes}", align="center", font=("Courier", 14, "bold"))
