from setuptools import setup, find_packages

setup(
    name="PixelPhantomX",
    version="1.0.0",
    author="Aditya Bhatt",
    author_email="info.adityabhatt3010@gmail.com",
    description="A tool for generating ghost images to confuse AI models.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AdityaBhatt3010/PixelPhantomX",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "pillow",
        "piexif",
        "pyfiglet",
        "termcolor"
    ],
    entry_points={
        "console_scripts": [
            "PixelPhantomX=PixelPhantomX:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
