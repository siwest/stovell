import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stovell-pkg-swest",
    version="0.0.1",
    author="Sarah West",
    author_email="sarah.irene.west@gmail.com",
    description="A small package for Stovell Research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siwest/stovell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)