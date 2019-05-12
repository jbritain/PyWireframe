PyWireframe
===========

PyWireframe is a Python library for creating 3D wireframe graphics. It's highly
inefficient (it uses turtle graphics) and doesn't support rotation.

Installation
------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
PyWireframe.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install PyWireframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage
-----

**Shapes:** PyWireframe has several shape functions built in, but you can also
define your own. Currently built-in shapes are:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cube(x, y, z, size) # a cube
cuboid(x, y, z, length, height, breadth) # a cuboid
pyramid3(x, y, z, size) # a 3 sided pyramid
pyramid4(x, y, z, size) # a 4 sided pyramid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also define your own shapes with the

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
line(x1, y1, z1, x2, y2, z2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

function, e.g

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def square:
    line(0, 0, 0, 100, 0, 0)
    line(0, 0, 0, 0, 100, 0)
    line(100, 100, 0, 100, 0, 0)
    line(100, 100, 100, 0, 0, 0)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Some syntax:**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import PyWireframe

PyWireframe.start() # starts PyWireframe
PyWireframe.exit() # closes the PyWireframe window
PyWireframe.refresh() 3
PyWireframe.cube(0, 0, 0, 100) # draws a cube with the left-bottom-front corner is at 0, 0, 0 and size 100
PyWireframe.CameraX += 1 # moves the camera forward 1 on the z axis
PyWireframe.FocalLength += 1 # changes the Focal Length by 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example code:**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import PyWireframe
def redraw(): 
PyreFrame.refresh() 
cube(0, 0, 0, 100) 
pyramid4(0, 100, 0, 100)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

License
-------

[MIT](https://choosealicense.com/licenses/mit/)
