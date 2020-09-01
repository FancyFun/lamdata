import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md","r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-FancyFun",
    version="0.0.2",
    author="FancyFun",
    description="something about makingn code",
    long_description=LONG_DESCRIPTION,
    long_description_markdown="Text/MarkDown",
    url="https://github.com/FancyFun/lamdata",
    packages=setuptools.find_packages(),
    python_version=">=3.6",
    install_require=REQUIRED,
    Classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ]


)
