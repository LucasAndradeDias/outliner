from setuptools import setup, find_packages



with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name="outliner-tracer",
    description="A tracer for compiled objects",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="MIT",
    url="https://github.com/LucasAndradeDias/outliner",
    version="1.3.0a1",
    keywords=["tracer","outliner","tracing","complex","objects"],
    author="Lucas A. Dias",
    author_email="lucasan1234565@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',  
    entry_points={
        "console_scripts": [
            "outliner = outliner.cli:main",
        ],
    },
)
