import tkinter as tk
import turtle

rules = [
    'F[+F]F[-F]F',
    'F[+F]F',
    'F[-F]F',
    'F[+F]F[-F][F]'
]

# Aqui se guardan los parametros de posicion y angulo
turtleValuesStack = []

'''
    Genera una cadena L-System a partir de:
        Conjunto de Reglas
        Axioma
        Numero de iteraciones
'''
def createLSystem(ruleList, axiom, numIterations):
    startString = axiom
    endString = ''
    for _ in range(numIterations):
        endString = processString(ruleList, startString)
        startString = endString
    return endString

'''
    Reemplaza la cadena anterior por la generada
'''
def processString(ruleList, oldString):
    newString = ''
    for symbol in oldString:
        newString = newString + applyRule(ruleList, symbol)
    return newString

def applyRule(ruleList, symbol):
    newString = ''
    if symbol == 'F':
        newString = ruleList[3]
    else:
        newString = symbol
    return newString

def drawLSystem(turt, lSystem, angle, distance):
    for symbol in lSystem:
        if symbol == 'F':
            turt.forward(distance)
        if symbol == '-':
            turt.right(angle)
        if symbol == '+':
            turt.left(angle)
        if symbol == '[':
            saveAngle = turt.heading()
            savePosition = [turt.xcor(), turt.ycor()]
            turtleValuesStack.append((saveAngle, savePosition))
        if symbol == ']':
            lastAngle, lastPosition = turtleValuesStack.pop()
            turt.setheading(lastAngle)
            turt.penup()
            turt.goto(lastPosition)
            turt.pendown()



def main():
    axiom = 'F'
    angle = 20
    iterations = 5
    distance = 5
    
    window.tracer(0)
    
    turt.up()
    turt.goto(0,-150)
    turt.setheading(90)
    turt.down()
    turt.speed('fastest')

    inst = createLSystem(rules, axiom, iterations)
    print(inst, "\n", '='*50)
    drawLSystem(turt, inst, angle, distance)
    turt.hideturtle()
    window.update()


root = tk.Tk()
root.geometry('500x675')
canvas = tk.Canvas(root, width = 400, height = 650)
canvas.grid(row = 0, columnspan = 6, pady = 10, padx = 10)
btn = tk.Button(root, text = "Generar", command = main)
btn.grid(row = 0, column = 8)

window = turtle.TurtleScreen(canvas)
window.bgcolor('black')
turt = turtle.RawTurtle(window)
turt.color('white')
root.mainloop()
