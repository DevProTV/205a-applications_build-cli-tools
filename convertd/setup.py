from setuptools import setup


setup(
    name = 'convertd',
    version = '0.1.0',
    packages = ['convertd'],
    entry_points = {
        'console_scripts': [
            'convertd = convertd.__main__:main'     
        ] 
    }
)
