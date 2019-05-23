import sys

#Define 3D Rendering Variables
global CameraX, CameraY, CameraZ, FocalLength

FocalLength = 100
CameraX = 0
CameraY = 0
CameraZ = 0
Objects = []

def start():

    print("Starting PyWireframe")
    print("Importing Modules") 

    import turtle
        
    print("Defining render")

    #Define render
    global render
    
    render=turtle.Turtle()
    render.speed(0)
    render.hideturtle()
    render.screen.title("PyWireframe")
    print("PyWireframe has started succesfully!")

#Redraw all predefined objects
def refresh():
    render.clear()

    for a in Objects:
        exec(a)

def exit():
    render.bye()

def addObject(shape, x, y, z, size):
    print("Added " + str(shape) + " object at " + str(x) + ", " + str(y) + ", " + str(z) + " as object #" + str(len(Objects)))
    Objects.append(str(shape) + "(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(size) + ")")

def addDynamicObject(function):
    print("Added '" + function + "' object as object #" + str(len(Objects)))
    Objects.append(function)

def deleteObject(value):
    Objects.pop(value)
    print("Deleted object #" + value)

def printObject(value):
    print(str(value) + ": " + str(Objects[value]))
    

#Define some shapes
def cube(x, y, z, size):
    line(x, y, z, x + size, y, z)
    line(x + size, y, z, x + size, y + size, z)
    line(x + size, y + size, z, x, y + size, z)
    line(x, y + size, z, x, y, z)

    line(x, y, z + size, x + size, y, z + size)
    line(x + size, y, z + size, x + size, y + size, z + size)
    line(x + size, y + size, z + size, x, y + size, z + size)
    line(x, y + size, z + size, x, y, z + size)

    line(x, y, z, x, y, z + size)
    line(x + size, y, z, x + size, y, z + size)
    line(x + size, y + size, z, x + size, y + size, z + size)
    line(x, y + size, z, x, y + size, z + size)

def pyramid3 (x, y, z, size):
    line(x, y, z, x + size, y, z)
    line(x, y, z, x + size / 2, y + size, z)
    line(x, y, z, x + size / 2, y, z + size)

    line(x + size, y, z, x + size / 2, y + size, z)
    line(x + size, y, z, x + size / 2, y, z + size)

    line(x + size / 2, y, z + size, x + size / 2, y + size, z)

def pyramid4 (x, y, z, size):
    line(x, y, z, x + size, y, z)
    line(x, y, z, x, y, z + size)

    line(x + size, y, z + size, x + size, y, z)
    line(x + size, y, z + size, x, y, z + size)

    line(x, y, z, x + size / 2, y + size, z + size / 2)
    line(x + size, y, z, x + size / 2, y + size, z + size / 2)
    line(x, y, z + size, x + size / 2, y + size, z + size / 2)
    line(x + size, y, z + size, x + size / 2, y + size, z + size / 2)

#Renders a line in 3d space
def line(x1, y1, z1, x2, y2, z2):

    try:
        ScaleFactor = FocalLength/(z1 - CameraZ + FocalLength)
    except ZeroDivisionError:
        ScaleFactor = 0

    X = (x1 - CameraX) * ScaleFactor
    Y = (y1 - CameraY) * ScaleFactor

    render.goto(X, Y)
    render.pendown()

    try:
        ScaleFactor = FocalLength/(z2 - CameraZ + FocalLength)
    except ZeroDivisionError:
        ScaleFactor = 0

    if ScaleFactor > 0:
        X = (x2 - CameraX) * ScaleFactor
        Y = (y2 - CameraY) * ScaleFactor

    render.goto(X, Y)
    render.penup()

def moveCamera(axis, amount):
    global CameraX
    global CameraY
    global CameraZ

    if axis == "X":
        CameraX += amount
    elif axis == "Y":
        CameraY += amount
    elif axis == "Z":
        CameraZ += amount
    else:
        raise Exception(axis +" is not a valid axis")

def debug():
    print("CameraX = " + str(CameraX))
    print("CameraY = " + str(CameraY))
    print("CameraZ = " + str(CameraZ))
    print("FocalLength = " + str(FocalLength))
    print("objects: ")
    print(Objects)
