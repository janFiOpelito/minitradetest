"""Setup file for minitrade project"""

import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="minitradetest",
    version="0.1.0",
    description=" minitrade project, a minimalist trade engine",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/janFiOpelito/minitradetest.git",
    author="jphdsn",
    author_email="jphdsn@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    keywords="sphinx",
    packages=setuptools.find_packages(include=["minitradetest","minitrade.*"])
    python_requires=">=3.8"
)
