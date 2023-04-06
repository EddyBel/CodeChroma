from setuptools import setup

readme = open("./README.md", "r")

setup(
    name="CodeChroma",
    packages=["CodeChroma"],
    version=1.0,
    description="This project is a simple library to color text in the terminal with python.",
    long_description=readme.read(),
    long_description_content_type="text/markdown",
    author="Eduardo Rangel",
    author_email="dante61918@gmail.com",
    url="https://github.com/EddyBel/CodeChroma",
    download_url="https://github.com/EddyBel/CodeChroma",
    keywords=["colors", "syntax", "terminal", "markdown"],
    classifiers=[ ],
    license="MIT",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[  
        "colorama==0.4.6",
        "colored==1.4.4",
        "Pygments==2.14.0",
        "termcolor==2.2.0",
    ],
)