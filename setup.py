from setuptools import setup, find_packages

setup(
    name="noor",                 # PyPI package name
    version="1.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "noor=noor.cli:main"
        ]
    },
    author="Noor",
    description="Live age calculator showing your life in seconds",
    python_requires=">=3.8",
)
