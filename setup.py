import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snakepixel-beta",
    version="0.1",
    author="TheLegendOfKitty",
    description="A python wrapper for the hypixel api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheLegendOfKitty/snakepixel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
