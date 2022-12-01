#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import HORIZONTAL, colorchooser
import turtle
class lSystem():
    def __init__(self, rules, axiom, iterations):
        self.rules = rules
        self.axiom = axiom
        self.iterations = iterations
        self.cadenaGenerada = [axiom]
        self.turtleValuesStack = []
    def prin(self):
        for i in rules:
            print(i[0], "->", i[1])
    
    def createLSystem(self):
        startString = self.axiom
        endString = ''
        for _ in range(self.iterations):
            endString = self.processString(startString)
            startString = endString
            self.cadenaGenerada.append(endString)
        # self.cadenaGenerada = endString
        
    '''
        Reemplaza la cadena anterior por la generada
    '''
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

    def cadena(self):
        print(self.cadenaGenerada)

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

    
                
rules = [
    ('F','F[+F]F[-F]F'),
    ('F','F[+F]F'),
    ('F','F[-F]F'),
    ('F','F[+F]F[-F][F]'),
    ('F','F[+F[-F]][-F]')
]

# rules = [
#     ('X', 'F[+X][-X]FX'),
#     ('F', 'FF')
# ]

def main():
   
    
    window.tracer(0)
    turt.clear()
    turt.width(width.get())
    turt.up()
    turt.goto(0,-250)
    turt.setheading(90)
    turt.down()
    turt.speed('fastest')

    inst = lSystem(rules, 'F', numIteraciones.get())
    inst.createLSystem()
    # system('cls')
    # print(inst)
    inst.drawLSystem(turt, angle.get(), dist.get())
    turt.hideturtle()
    window.update()


def fondo():
    color_selec = colorchooser.askcolor()
    window.bgcolor(color_selec[1])
def lapiz():
    color_selec = colorchooser.askcolor()
    turt.color(color_selec[1])

root = tk.Tk()
root.geometry('700x675')
canvas = tk.Canvas(root, width = 400, height = 650)
canvas.grid(row = 0, columnspan = 6, rowspan= 100, pady = 10, padx = 10)
btnGenerar = tk.Button(root, text = 'Generar', command = main)
btnGenerar.grid(row = 0, column = 8)
btnBgColor = tk.Button(root, text = 'Color de fondo', command = fondo)
btnBgColor.grid(row = 1, column = 8)
btnBgColor = tk.Button(root, text = 'Color de dibujo', command = lapiz)
btnBgColor.grid(row = 2, column = 8)

lblIteraciones = tk.Label(root, text = "Iteraciones")
lblIteraciones.grid(row = 0, column = 9)
numIteraciones = tk.Scale(root, from_=0, to=7, orient=HORIZONTAL)
numIteraciones.grid(row = 1, column= 9)
numIteraciones.set(3)

lbldist = tk.Label(root, text = "Distancia")
lbldist.grid(row = 2, column = 9)

dist = tk.Scale(root, from_=1, to=10, orient=HORIZONTAL)
dist.grid(row = 3, column= 9)
dist.set(5)

lblwidth = tk.Label(root, text = "Grosor")
lblwidth.grid(row = 4, column = 9)

width = tk.Scale(root, from_=1, to=5, orient=HORIZONTAL)
width.grid(row = 5, column= 9)
width.set(1)

lblangle = tk.Label(root, text = "Ángulo")
lblangle.grid(row = 6, column = 9)
angle = tk.Scale(root, from_=-90, to=90, orient=HORIZONTAL)
angle.grid(row = 7, column= 9)

window = turtle.TurtleScreen(canvas)
window.bgcolor('black')
turt = turtle.RawTurtle(window)
turt.color('white')
root.mainloop()