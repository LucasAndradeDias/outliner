from setuptools import setup, find_packages


setup(
    name="outliner",
    description="A tracer for compiled objects",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "outliner = outliner.cli:main",
        ],
    },
)
