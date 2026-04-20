#Icker Santiago Alba Ayala
import turtle
import time
 
# Configuración de pantalla
pantalla = turtle.Screen()
pantalla.title("🚀 Cohete en movimiento")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)
 
# --- Dibujar estrellas de fondo ---
estrella = turtle.Turtle()
estrella.hideturtle()
estrella.penup()
estrella.color("white")
 
import random
random.seed(42)
for _ in range(80):
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    estrella.goto(x, y)
    estrella.dot(random.choice([2, 3, 4]))
 
# --- Dibujar el cohete ---
cohete = turtle.Turtle()
cohete.hideturtle()
cohete.penup()
cohete.speed(0)
 
def dibujar_cohete(t, x, y):
    t.clear()
    t.penup()
 
    # Cuerpo del cohete
    t.goto(x, y)
    t.pendown()
    t.color("white", "lightblue")
    t.begin_fill()
    t.goto(x - 15, y)
    t.goto(x - 15, y + 50)
    t.goto(x, y + 70)
    t.goto(x + 15, y + 50)
    t.goto(x + 15, y)
    t.goto(x - 15, y)
    t.end_fill()
 
    # Ventana del cohete
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.color("cyan", "cyan")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
 
    # Ala izquierda
    t.penup()
    t.goto(x - 15, y + 10)
    t.pendown()
    t.color("white", "red")
    t.begin_fill()
    t.goto(x - 30, y - 10)
    t.goto(x - 15, y + 20)
    t.goto(x - 15, y + 10)
    t.end_fill()
 
    # Ala derecha
    t.penup()
    t.goto(x + 15, y + 10)
    t.pendown()
    t.color("white", "red")
    t.begin_fill()
    t.goto(x + 30, y - 10)
    t.goto(x + 15, y + 20)
    t.goto(x + 15, y + 10)
    t.end_fill()
 
    # Fuego del cohete
    t.penup()
    t.goto(x - 8, y)
    t.pendown()
    t.color("orange", "yellow")
    t.begin_fill()
    t.goto(x, y - random.randint(20, 40))
    t.goto(x + 8, y)
    t.end_fill()
 
# --- Animación de vuelo ---
y_pos = -250
 
while y_pos < 320:
    dibujar_cohete(cohete, 0, y_pos)
    pantalla.update()
    y_pos += 3
    time.sleep(0.02)
 
# Mensaje final
mensaje = turtle.Turtle()
mensaje.hideturtle()
mensaje.penup()
mensaje.goto(0, 0)
mensaje.color("yellow")
mensaje.write("🚀 ¡Despegue exitoso!", align="center", font=("Arial", 18, "bold"))
pantalla.update()
 
pantalla.mainloop()
 
