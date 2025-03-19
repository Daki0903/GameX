from setuptools import setup, find_packages

setup(
    name="gamex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pygame"],
    author="David",
    author_email="nesicking@gmail.com",
    description="Simple 2d engine for 2d games",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tvoj_github/gamex",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
