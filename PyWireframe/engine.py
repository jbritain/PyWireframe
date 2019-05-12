import sys

#Define 3D Rendering Variables
global CameraX
global CameraY
global CameraZ
global FocalLength

FocalLength = 100
CameraX = 0
CameraY = 0
CameraZ = 0

def start():

    print("PyWireframe: Starting PyWireframe")
    print("PyWireframe: Importing Modules") 

    try:
        import turtle
    except ImportError:
        print("PyWireframe: Error importing modules. Make sure you have the Turtle module installed.")
        sys.exit()

    print("PyWireframe: Defining render")

    #Define render
    global render
    
    render=turtle.Turtle()
    render.speed(0)
    render.hideturtle()
    render.screen.title("PyWireframe")
    print("PyWireframe: PyWireframe has started succesfully!")

#Define the lines to render
def refresh():
    render.clear()

def exit():
    render.bye()

#Define some shapes
def cube(x, y, z, size):
    line(x, y, z, size, y, z)
    line(size, y, z, size, size, z)
    line(size, size, z, y, size, z)
    line(x, size, z, x, y, z)

    line(x, y, size, size, y, size)
    line(size, y, size, size, size, size)
    line(size, size, size, x, size, size)
    line(x, size, size, x, y, size)

    line(x, y, z, x, y, size)
    line(size, y, z, size, y, size)
    line(size, size, z, size, size, size)
    line(x, size, z, x, size, size)

def pyramid3 (x, y, z, size):
    line(x, y, z, size, y, z)
    line(x, y, z, size / 2, size, z)
    line(x, y, z, size / 2, y, size)

    line(size, y, z, size / 2, size, z)
    line(size, y, z, size / 2, y, size)

    line(size / 2, y, size, size / 2, size, z)

def pyramid4 (x, y, z, size):
    line(x, y, z, size, y, z)
    line(x, y, z, x, y, size)

    line(size, y, size, size, y, z)
    line(size, y, size, x, y, size)

    line(x, y, z, size / 2, size, size / 2)
    line(size, y, z, size / 2, size, size / 2)
    line(x, y, size, size / 2, size, size / 2)
    line(size, y, size, size / 2, size, size / 2)

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
