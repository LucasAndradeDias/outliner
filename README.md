# Outliner

Have you ever got confused trying to understand python complex object invoking sequence?! Now it is a solved problem.

Outliner is a Python utility designed to simplify the process of tracing the calling flow of callable objects within a complex Python object. It aims to help developers understand the order in which callable objects are invoked within complex code structures, making it easier to navigate and comprehend such structures.



## Table of Contents
- [Example](#example)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Example

We have the given complex object:
```python
class test:
    def __init__(self) -> None:
        self.func1()
    def func1(self):
        self.func2()
        return
    def func2(self):
        return
def test2():
    a = test()
    return
``` 

With the outliner you can visualize the invoking flow in order with the default tree display:
```
 outliner --file_path=path-to-module --object_invoke="test()"
```
output:
```bash
    test2
    │
    │──1. __init__                                          module_testing_1.py     2
    │
    │──2. func1                                             module_testing_1.py     5
    │
    │──3. func2                                             module_testing_1.py     9
```

(If some exception was raised while tracing, the broken object will appear write in red color.)

Get more detailed data about invoked objects (-d="detailed_data"):
```
 outliner --file_path=path-to-module --object_invoke="test()" -d="detailed_data"
```
output:
```bash
        Invoked objects: 2

        - test2:
            lines: 2
            called: 1
            return: 1
        - __init__:
            lines: 3
            called: 1
            return: 1
```


## Features

-   **Function Tracing**: Trace function calls, returns, and line execution within a Python module.
-   **Data Collection**: Collect detailed data on function executions and execution flow.
-   **Method Tree**: Display a tree of functions used by the object for object behavior exploration.
-   **Easy Integration**: Simple and straightforward integration into your Python projects.
-   **Customizable**: Fine-tune tracing parameters to suit your debugging and exploration

## Installation
As the library hasn't been released yet, to use it on your machine, you will need to do following steps:

-	**Use pip install:**
	Make sure that path contains the setup.py file
	``` 
	pip install -i outliner-tracer
	```
-	**Install from github:**
	``` 
	pip install git+https://github.com/LucasAndradeDias/outliner
 	```
-	**Clone from github and install locally:**
	``` 
	git clone https://github.com/LucasAndradeDias/outliner
 	pip install ./outliner
	```


## Usage

The Outliner library can be used via the command-line interface (CLI) to trace Python code. Follow these steps to use it:

1.  Open your terminal.
    
2.  Run the following command to trace a Python object's execution:
    

bashCopy code

`outliner --file_path=<path-to-object> --object_invoke=<object-invoking>` 

## Python supported versions
Outliner is compatible with Python versions 3.6 to 3.12.


## Command Line Options

-   `--file_path`(Required): Specifies the path to the Python module containing the object to be traced.
    
-   `--object_invoke | -o `(Required): The invoking stetament of the object you want to trace.
    
-   `--mode`(Optional): The output mode (tree or detaield_data).

## Contributing

Contributions to the Outliner library are welcome. If you have ideas for improvements, find any issues, or want to contribute to its development, please open an [issue](https://github.com/your-repo/issues) or submit a [pull request](https://github.com/your-repo/pulls) on GitHub.
