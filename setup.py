from setuptools import setup

setup(
    name='scrawl',
    version='1',
    py_modules=['click_version'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        scrawl=click_version:scrawl
    ''',
)
