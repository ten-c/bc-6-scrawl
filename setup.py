from setuptools import setup

setup(
    name='scrawl',
    version='1',
    py_modules=['scrawl'],
    install_requires=[
        'Click',
        'python-firebase',
    ],
    entry_points='''
        [console_scripts]
        scrawl=scrawl:scrawl
    ''',
)
