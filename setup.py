'''
setup.py
'''

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()



setuptools.setup(
    name='pymitblod',
    version="0.0.1",
    author='Christian Skjerning',
    author_email='christian@skjerning.eu',
    description='API wrapper for blood donor webpages.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/slimcdk/pymitblod',
    project_urls={
        "Bug Tracker": "https://github.com/slimcdk/pymitblod/issues",
    },
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)