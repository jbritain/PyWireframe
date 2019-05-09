 
![enter image description here](https://lh3.googleusercontent.com/XQoxcWLR4Fi8OXt22lIu_TESMA3kzHFIWOjiNFOfJ5uqOzXTDPdyYKhBB800oZ8HxcHfeOCBjOxO=s50)  PyWireframe 
========================================

PyWireframe is a Python library for creating 3D wireframe graphics. It's highly inefficient (it uses turtle graphics) and doesn't support rotation.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyWireframe.

```bash
pip install PyWireframe
```

## Usage


**Shapes:**
PyWireframe has several shape functions built in, but you can also define your own. Currently built-in shapes are:
```Python
cube(x, y, z, size) # a cube
pyramid3(x, y, z, size) # a 3 sided pyramid
pyramid4(x, y, z, size) # a 4 sided pyramid
```
You can also define your own shapes with the 

    line(x1, y1, z1, x2, y2, z2)
function, e.g

```python
def square:
	line(0, 0, 0, 100, 0, 0)
	line(0, 0, 0, 0, 100, 0)
	line(100, 100, 0, 100, 0, 0)
	line(100, 100, 100, 0, 0, 0)
```

**Some syntax:**
```python
import PyWireframe

PyWireframe.start() # starts PyWireframe
PyWireframe.exit() # closes the PyWireframe window
PyWireframe.refresh() 3

PyWireframe.cube(0, 0, 0, 100) # draws a cube where the left-bottom-front corner is at 0, 0, 0 and the size is 100
pyramid4(0, 100, 0, 100) # draws a 4-sided pyramid where the left-bottom-front corner is at 0, 0, 0 and the size is 100
PyWireframe.CameraX += 1 # moves the camera forward 1 on the z axis
PyWireframe.FocalLength += 1 # changes the Focal Length by 1
```

**Example code:**
```python
import PyWireframe

def redraw(): 
	PyreFrame.refresh() 
	cube(0, 0, 0, 100) 
	pyramid4(0, 100, 0, 100)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

