#Icker Santiago Alba Ayala
import turtle
import random
 
# Configuración
pantalla = turtle.Screen()
pantalla.title("Estrella de Colores - Turtle")
pantalla.bgcolor("black")
pantalla.setup(width=600, height=600)
 
lapiz = turtle.Turtle()
lapiz.speed(0)
lapiz.width(2)
 
colores = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta"]
 
# Dibujar espiral de estrellas
for i in range(200):
    lapiz.color(colores[i % len(colores)])
    lapiz.forward(i * 0.5)
    lapiz.right(91)
 
lapiz.hideturtle()
pantalla.mainloop()
