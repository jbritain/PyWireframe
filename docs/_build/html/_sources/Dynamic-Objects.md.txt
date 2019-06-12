# Dynamic Objects

## What are they?
Added in version 0.4, dynamic objects are similar to normal [objects](https://github.com/HyperHamster535/PyWireframe/wiki/Objects), but they allow [shapes](https://github.com/HyperHamster535/PyWireframe/wiki/Shapes) with custom parameter layouts.

## Usage
To create a dynamic object, use the `createDynamicObject(function)` function. The `function` parameter should be the code to execute a shape function, e.g `createDynamicObject("cuboid, 0, 0, 0, 100, 50, 50")`. **_The `function` parameter must be in speech marks._**