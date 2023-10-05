
# Outliner (Alpha)

Have you ever found an python complex object that you get lost trying to undestand the invoking sequence?! Now it is a solved problem.


Outliner is a Python utility that simplifies the process of tracing the calling flow of callable objects within a complex object. It helps you understand the order in which these callable objects are invoked, making it easier to navigate and comprehend complex code structures.

## Table of Contents
- [Example](#example)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Example

We have the given complex object:
```
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

With the outliner you can visualyze the invoking flow in order with the default tree display:
```
 outliner --file_path=path-to-module --object_name=test
```

```
    test2
    │
    │──1. __init__
    │
    │──2. func1
    │
    │──3. func2
```

Or get more detailed data about invoked objects (-d="detailed_data"):
```
 outliner --file_path=path-to-module --object_name=test --d="detailed_data"
```
output:
```
('test2', {'call': 1, 'return': 1, 'line': 2})
('__init__', {'call': 1, 'return': 1, 'line': 1})
('func1', {'call': 1, 'return': 1, 'line': 2})
('func2', {'call': 1, 'return': 1, 'line': 1})
```


## Features

-   **Function Tracing**: Trace function calls, returns, and line execution within a Python module.
-   **Data Collection**: Collect detailed data on function executions and execution flow.
-   **Method Tree**: Display a tree of methods used by the object for object behavior exploration.
-   **Easy Integration**: Simple and straightforward integration into your Python projects.
-   **Customizable**: Fine-tune tracing parameters to suit your debugging and exploration

## Installation
As the library hasn't been released yet, to use it on your machine, you will need to do following steps:

-	**Use pip install:**
	Make sure that path contains the setup.py file
	``` 
	pip install -i https://test.pypi.org/simple/ outliner
	```

## Usage

The Outliner library can be used via the command line interface (CLI) to trace Python code. Follow the steps below to use it:

1. Open your terminal.

2. Run the following command to trace a Python object's execution:

```bash
outliner --file_path=<path-to-object> --object_name=<object-name> --object_args=<arguments-passed-to-object>
```

## Contributing

Contributions to the Outliner library are welcome. If you have ideas for improvements, find any issues, or want to contribute to its development, please open an [issue](https://github.com/your-repo/issues) or submit a [pull request](https://github.com/your-repo/pulls) on GitHub.
