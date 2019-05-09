 
![enter image description here](https://lh3.googleusercontent.com/XQoxcWLR4Fi8OXt22lIu_TESMA3kzHFIWOjiNFOfJ5uqOzXTDPdyYKhBB800oZ8HxcHfeOCBjOxO=s50)  **PyWireframe**  
========================================

What is it?

PyWireframe is a wireframe graphics engine I wrote in which uses turtle graphics.
It is highly inefficient, unrealistic, and does not support rotation of any
kind.

Using it
========

PyWireframe can be used as a module in other programs. The syntax is as follows:

**Shapes**

-   **Cube(X, Y, Z, Size)**: Creates a cube at specified coordinates with
    specified size. The origin of the cube is the front-bottom-left corner.

-   **Pyramid3(X, Y, Z, Size)**: Creates a 3-sided pyramid at specified
    coordinates with specified size. The origin of the 3-sided pyramid is the
    front-bottom-left corner.

-   **Pyramid4(X, Y, Z, Size)**: Creates a 4-sided pyramid at specified
    coordinates with specified size. The origin of the 4-sided pyramid is the
    front-bottom-left corner.

-   **Line(X1, Y1, Z1, X2, Y2, Z2)**: Creates a line from the first set of
    coordinates to the second one.

**Other syntax**

-   **Refresh()**: Clears the display. To redraw the shapes, just re-run all of
    the shape functions specified, e.g
    
    def redraw():
	    PyreFrame.refresh()
	    cube(0, 0, 0, 100)
	    herepyramid4(0, 100, 0, 100)

-   **Start()**: Starts the PyreFrame window. You can’t use PyWireframe until
    PyWireframe.start() has been called.

-   **Exit()**: Closes the PyWireframe window.

**Variables**

-   **CameraX**: X position of the camera.

-   **CameraY**: Y position of the camera.

-   **CameraZ**: Z position of the camera.

-   **FocalLength**: It’s the focal length. I don’t know what it really does (I
    didn’t work out the maths!), it’s kind of like the FOV I guess?

