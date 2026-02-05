from setuptools import setup, find_packages

setup(
    name="noor-cli",                 # PyPI package name
    version="1.0.2",
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
