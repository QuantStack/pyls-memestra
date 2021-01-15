from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyls-memestra",
    version="0.0.11",
    description="Memestra plugin for the Python Language Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QuantStack/pyls-memestra",
    author="marimeireles",
    author_email="mariana@psychonautgirl.space",
    packages=['pyls_memestra', "tests"],
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={"pyls": ["pyls_memestra = pyls_memestra.plugin"]},
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
