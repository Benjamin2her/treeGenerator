#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas, Button, Scale, colorchooser, HORIZONTAL, FLAT
import turtle
import random

# Boton personalizado
class Boton(Button):
    def __init__(self, row, column, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.config(
            background = '#282a36',
            foreground = '#f8f8f2',
            activeforeground= '#282a36',
            activebackground = '#50fa7b',
            border = '2px', 
            padx = 15, pady = 5, 
            font = ('monaco', 12),
            width = 12,
            height = 1,
            cursor = 'hand1',
            relief = FLAT
        )
        self.grid(row = row, column = column, columnspan = 1, rowspan = 1)

# Barra Escaladora personalizada
class Escaladora(Scale):
    def __init__(self, row, column, default, *args, **kwargs):
        Scale.__init__(self, *args, **kwargs)
        self.config(
            background = '#282a36',
            foreground = '#f8f8f2',
            activebackground= '#6272a4',
            troughcolor = '#50fa7b',
            length = 150,
            width = 13,
            sliderlength = 30,
            font = ('monaco', 10),
            orient = HORIZONTAL,
            relief = FLAT,
            repeatdelay = 100
        )
        self.grid(row = row, column = column, columnspan = 1, rowspan = 1)
        self.set(default)

# Sistema L que representa al arbol
class lSystem():
    def __init__(self, rules, axiom, iterations):
        self.rules = rules
        self.axiom = axiom
        self.iterations = iterations
        self.cadenaGenerada = [axiom]
        self.turtleValuesStack = []

        startString = self.axiom
        endString = ''
        for _ in range(self.iterations):
            endString = self.processString(startString)
            startString = endString
            self.cadenaGenerada.append(endString)

    # Reemplaza la cadena anterior por la generada
    def processString(self, oldString):
        newString = ''
        for symbol in oldString:
            newString = newString + self.applyRule(symbol)
        return newString

    def applyRule(self, symbol):
        newString = ''
        if symbol == 'F':
            value = random.randint(0,len(self.rules) - 1)
            newString = rules[value][1]
        else:
            newString = symbol
        return newString

    def drawLSystem(self, turt, angle, distance):
        for symbol in self.cadenaGenerada[self.iterations]:
            if symbol == 'F':
                turt.forward(distance)
            if symbol == '-':
                turt.right(angle)
            if symbol == '+':
                turt.left(angle)
            if symbol == '[':
                saveAngle = turt.heading()
                savePosition = [turt.xcor(), turt.ycor()]
                self.turtleValuesStack.append((saveAngle, savePosition))
            if symbol == ']':
                lastAngle, lastPosition = self.turtleValuesStack.pop()
                turt.setheading(lastAngle)
                turt.penup()
                turt.goto(lastPosition)
                turt.pendown()
            
# Reglas
rules = [
    ('F','F[+F]F[-F]F'),
    ('F','F[+F]F'),
    ('F','F[-F]F'),
    ('F','F[+F]F[-F][F]'),
    ('F','F[+F[-F]][-F]')
]


# genera y dibuja el lsystem
def generate():
    inst = lSystem(rules, 'F', escIteraciones.get())
    window.tracer(0)
    turt.clear()
    turt.width(escGrosor.get())
    turt.up()
    turt.goto(0,-300)
    turt.setheading(90)
    turt.down()
    inst.drawLSystem(turt, escAngulo.get(), escDistancia.get())
    window.update()


def cambiarColorFondo():
    color_selec = colorchooser.askcolor()
    try:
        window.bgcolor(color_selec[1])
    except:
        pass

def cambiarColorTortuga():
    color_selec = colorchooser.askcolor()
    try:
        turt.color(color_selec[1])
    except:
        pass

# Ventana principal
root = Tk()
root.geometry('577x663')
root.configure(background = '#44475a')
root.resizable(width=False, height=False)
root.title("Tree-Generator")

#Canvas dibujo
canvas = Canvas(root, width = 400, height = 650)
canvas.grid(row = 0, columnspan = 6, rowspan= 100, pady = 5, padx = 5)

# Botones Generar L-System, y cambio de color
btnGenerar = Boton(1, 8, root, text = 'Generar', command = generate)
btnBgColor = Boton(2, 8, root, text = 'Color de fondo', command = cambiarColorFondo)
btnFgColor = Boton(3, 8, root, text = 'Color de dibujo', command = cambiarColorTortuga)

# Parametros del arbol
escIteraciones = Escaladora(4, 8,  5, root, from_=  0, to =  7, label = "Iteraciones")
escDistancia   = Escaladora(5, 8,  5, root, from_=  1, to = 10, label = "Distancia")
escGrosor      = Escaladora(6, 8,  1, root, from_=  1, to =  3, label = "Grosor")
escAngulo      = Escaladora(7, 8, 25, root, from_=-90, to = 90, label = "Ángulo")

# Ventana de la tortuga
window = turtle.TurtleScreen(canvas)
window.bgcolor('black')
# Tortuga
turt = turtle.RawTurtle(window)
turt.color('lightgreen')
turt.hideturtle()

root.mainloop()