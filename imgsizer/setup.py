from setuptools import setup, find_packages

setup(
    name = 'imgsizer',
    version = '0.1.0',
    packages = ['imgsizer'],
    entry_points = {
        'console_scripts': [
            'imsizer = imgsize.__main__:main'     
        ]
    },
    packages = find_packages()
)
