from setuptools import setup, find_packages

setup(
    name="imgsizer",
    version="0.1.0",
    packages=["imgsizer"],
    entry_points={"console_scripts": ["imgsizer = imgsizer.__main__:main"]},
)
