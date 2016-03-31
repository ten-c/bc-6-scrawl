from setuptools import setup

setup(
    name='scrawl',
    version='1',
    py_modules=['scrawl','scrawl2'],
    install_requires=[
        'Click',
        'python-firebase',
    ],
    entry_points='''
        [console_scripts]
        scrawl=scrawl:scrawl
        scrawl2=scrawl2:scrawl
    ''',
)
