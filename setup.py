from setuptools import setup, find_packages
import codecs
import os

with open("README.md", "r") as f:
    long_description = f.read()

VERSION = '0.0.22'
DESCRIPTION = 'Data science package'

# Setting up
setup(
    name='dstricks',
    version=VERSION,
    author="RJUNCC (Ryan Jacobs)",
    author_email='ryan.jacobs04@outlook.com',
    description=DESCRIPTION,
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[ 
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ],
    install_requires=["pandas", "numpy", "scikit-learn", "seaborn", "matplotlib", "scipy", "statsmodels"],
    keywords=['python', 'data science', 'ds', 'functions'],
    extras_require={
        'dev':['pytest>=7.0', "twine>=5.0.0"]
    },
    python_requires='>=3.10'
)