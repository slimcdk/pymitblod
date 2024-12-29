'''
setup.py
'''

import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="pyprosang",
    version_config={
        "template": "{tag}",
    },
    author="Christian Skjerning",
    author_email="christian@skjerning.eu",
    description="API wrapper for blood donor webpages powereded by ProSang.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/slimcdk/pyprosang",
    install_requires=[
        "requests==2.32.3",
        "BeautifulSoup4==4.12.3"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/slimcdk/pyprosang/issues",
    },
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    setup_requires=['setuptools-git-versioning'],
)