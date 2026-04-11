from setuptools import setup

setup(
    name='Count Letters CLI',
    version='1.0',
    py_modules=['task1'],
    install_requires=[
        'docopt',
    ],
    entry_points = {
        'console_scripts':[
            'task1 = task1:main',
        ]
    }
)