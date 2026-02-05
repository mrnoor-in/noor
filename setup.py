from setuptools import setup, find_packages

setup(
    name="noor-cli",                 # PyPI name (unique)
    version="1.0.4",                 # change for every release
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "noor=noor.cli:main"     # user runs: noor
        ]
    },
    author="Noor",
    description="Live age calculator showing life in seconds",
    python_requires=">=3.8",
)
