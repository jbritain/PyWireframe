import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyWireframe",
    version="0.1.0",
    author="HyperHamster534",
    author_email="joshua@the-britains.com",
    description="PyreFrame is a wireframe 3D graphics engine which uses turtle graphics. It is highly inefficient, unrealistic, and does not support rotation of any kind.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HyperHamster535/PyWireframe/",
    packages=['PyWireframe'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
