import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vaw",
    version="0.0.1",
    author="VoidHub Stift007",
    author_email="stift007@stift007.de",
    description="Python Wrapper for VoidHub's API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voidhubapp/vaw",
    project_urls={
        "Bug Tracker": "https://github.com/voidhubapp/vaw/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=["requests"]
)