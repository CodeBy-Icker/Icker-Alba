#Icker Santiago Alba Ayala
import turtle
import math
 
# Configuración
pantalla = turtle.Screen()
pantalla.title("🌍 Planeta orbitando al Sol")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)
 
# --- Estrellas de fondo ---
fondo = turtle.Turtle()
fondo.hideturtle()
fondo.penup()
fondo.color("white")
 
import random
random.seed(10)
for _ in range(100):
    fondo.goto(random.randint(-290, 290), random.randint(-290, 290))
    fondo.dot(random.choice([1, 2, 3]))
 
# --- Sol ---
sol = turtle.Turtle()
sol.hideturtle()
sol.penup()
sol.goto(0, -20)
sol.pendown()
sol.color("yellow", "orange")
sol.begin_fill()
sol.circle(40)
sol.end_fill()
# Texto Sol
sol.penup()
sol.goto(0, 25)
sol.color("yellow")
sol.write("Sol", align="center", font=("Arial", 10, "bold"))
 
# --- Órbita (círculo guía) ---
orbita = turtle.Turtle()
orbita.hideturtle()
orbita.penup()
orbita.goto(0, -150)
orbita.pendown()
orbita.color("#333333")
orbita.circle(150)
 
# --- Planeta Tierra ---
tierra = turtle.Turtle()
tierra.shape("circle")
tierra.color("dodgerblue")
tierra.shapesize(1.5)
tierra.penup()
 
# --- Luna ---
luna = turtle.Turtle()
luna.shape("circle")
luna.color("lightgray")
luna.shapesize(0.6)
luna.penup()
 
# --- Rastro de la tierra ---
tierra.pendown()
tierra.color("dodgerblue")
tierra.pensize(1)
 
# --- Etiquetas ---
etiqueta = turtle.Turtle()
etiqueta.hideturtle()
etiqueta.penup()
 
# --- Animación ---
angulo = 0
angulo_luna = 0
 
while True:
    # Posición de la Tierra
    rad = math.radians(angulo)
    x_tierra = 150 * math.cos(rad)
    y_tierra = 150 * math.sin(rad)
    tierra.goto(x_tierra, y_tierra)
 
    # Posición de la Luna (orbita alrededor de la Tierra)
    rad_luna = math.radians(angulo_luna)
    x_luna = x_tierra + 35 * math.cos(rad_luna)
    y_luna = y_tierra + 35 * math.sin(rad_luna)
    luna.goto(x_luna, y_luna)
 
    # Etiqueta Tierra
    etiqueta.clear()
    etiqueta.goto(x_tierra, y_tierra + 15)
    etiqueta.color("white")
    etiqueta.write("Tierra", align="center", font=("Arial", 8, "normal"))
 
    etiqueta.goto(x_luna, y_luna + 10)
    etiqueta.color("lightgray")
    etiqueta.write("Luna", align="center", font=("Arial", 7, "normal"))
 
    pantalla.update()
 
    angulo += 1
    angulo_luna += 4
 
    if angulo >= 360:
        angulo = 0
 
pantalla.mainloop()
