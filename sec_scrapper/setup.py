import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sec_scrapper",
    version="0.0.11",
    author="Alex Bondoux",
    author_email="alexandre.bdx@gmail.com",
    description="Library for Insight project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexBdx/sec-scrapper/tree/master/sec-scrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
)
