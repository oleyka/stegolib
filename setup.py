from setuptools import setup, find_packages

setup(
    name='stegolib',
    version='0.1.dev0',
    packages=['stegolib'],
    license='The Unlicense',
    long_description=open('README.md').read(),
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-pep8'
    ],
)
