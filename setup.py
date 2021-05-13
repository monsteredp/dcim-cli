from setuptools import setup
setup(
    name='dcim',
    version='0.1.0',
    packages=['dcim'],
    entry_points={
        'console_scripts': [
            'dcim = dcim.__main__:main'
        ]
    })
