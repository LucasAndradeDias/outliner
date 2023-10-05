from setuptools import setup, find_packages


setup(
    name="outliner",
    description="A tracer for compiled objects",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license='MIT',
    url="https://github.com/LucasAndradeDias/outliner",
    version="1.2.0a1",
    keywords='Tracing complex callable objects',
    author='Lucas A. Dias',
    author_email='lucasan1234565@gmail.com',
    entry_points={
        "console_scripts": [
            "outliner = outliner.cli:main",
        ],
    },
)
