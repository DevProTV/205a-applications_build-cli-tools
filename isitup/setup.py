from setuptools import setup

setup(
    name="isitup",
    version="0.1.0",
    packages=['isitup'],
    entry_points={
        'console_scripts': [
            'isitup = isitup.__main__:main'
        ]     
    }
)
