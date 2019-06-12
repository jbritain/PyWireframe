PyWireframe V0.5
===========

PyWireframe is a Python library for creating 3D wireframe graphics. It's highly
inefficient (it uses turtle graphics) and doesn't support rotation.

Installation
------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install
PyWireframe.

# `pip install PyWireframe`

Usage
-----
PyWireframe has three different ways of rendering - [Objects](https://pywireframe.readthedocs.io/Usage/Objects), [Shapes](https://pywireframe.readthedocs.io/Usage/Shapes), and [Dyanmic Objects](https://pywireframe.readthedocs.io/Usage/Dynamic-Objects). For info on the syntax for using these, [see the official documentation](https://pywireframe.readthedocs.io/).
To start PyWireframe, use `start()`
To render all existing objects, use `refresh()`
To exit PyWireframe, use `exit()`
You can also stop PyWireframe from printing to the console with `printMode(mode)`. More info can be found on the [wiki](https://pywireframe.readthedocs.io/Usage/The-printMode(mode)-Function).

License
-------

[MIT](https://choosealicense.com/licenses/mit/)
