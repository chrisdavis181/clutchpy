from setuptools import setup
import clutchpy.version as version

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='clutchpy',
    version=version.__version__,
    description='A python client to interface with the Clutch API',
    packages=['clutchpy'],
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Chris Davis',
    url='https://github.com/chrisdavis181/clutchpy',
    author_email='chrisdavis179@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10'
)
