PyWireframe V0.3
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
**Objects:** Added in version 0.2, PyWireframe supports the creation of objects that will always be rendered. It uses the following syntax:

```python
createObject(shape, x, y, z, size) #Creates an object. The shape parameter can use any function defined in the format shown in the 'Shapes' section.
deleteObject(value) #Deletes the object asigned to the specified value. The number of an object is assigned when it is created.
printObject(value) #Prints the object associated with a specific value.
``````


**Shapes:** PyWireframe has several shape functions built in, but you can also
define your own. Currently built-in shapes are:

```python
cube(x, y, z, size) # a cube
pyramid3(x, y, z, size) # a 3 sided pyramid
pyramid4(x, y, z, size) # a 4 sided pyramid
```

You can also define your own shapes with the```line(x1, y1, z1, x2, y2, z2)```function, e.g

```python
def square:
    line(0, 0, 0, 100, 0, 0)
    line(0, 0, 0, 0, 100, 0)
    line(100, 100, 0, 100, 0, 0)
    line(100, 100, 100, 0, 0, 0)
```
but it must use the format:```def shape(x, y, z, size):```
for it to be used as an object.

**The Camera:** PyWireframe has a camera, which can be moved with```moveCamera(axis, amount)```. Bear in mind that ```axis``` must be in quotations, e,g ```moveCamera("X", 50)```

License
-------

[MIT](https://choosealicense.com/licenses/mit/)
