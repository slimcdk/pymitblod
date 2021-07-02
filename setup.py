'''
setup.py
'''
from os import path
from setuptools import setup
import pymitblod


THIS_DIRECTORY = path.abspath(path.dirname(__file__))

with open(path.join(THIS_DIRECTORY, 'readme.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='pymitblod',
    version=pymitblod.__version__,
    description='API wrapper for blood donor webpages.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/slimcdk/pymitblod',
    author='Christian Skjerning',
    author_email='christian@skjerning.eu',
    license='Apache 2.0',
    packages=['pymitblod'],
    install_requires=[
        'requests==2.25.1',
        'BeautifulSoup4==4.9.3'
    ]
)