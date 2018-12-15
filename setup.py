import sys

from setuptools import setup, find_packages

requires = ["click", "coloredlogs==10.0", "humanfriendly==4.17"]
tests_requires = ["pytest", "pytest-cache", "pytest-cov"]
lint_requires = ["flake8", "black"]
dev_requires = ["bumpversion"] + requires + tests_requires + lint_requires


setup(
    name="gypse",
    version="0.1.5",
    description="Gypse analyzes and reveals information of the text files that you have. It identifies things like URLs, E-Mails and Phone Numbers, which are difficult to extract.",
    long_description="\n\n".join([open("README.rst").read()]),
    license="MIT",
    author="David G. Daniel",
    author_email="davydany@aeroxis.com",
    url="https://gypse.readthedocs.org",
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "gypse = gypse.cli:gypse"
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    extras_require={"test": tests_requires, "dev": dev_requires, "lint": lint_requires},
)
