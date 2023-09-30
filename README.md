
# Outliner (Under development)

The Outliner library is a Python tool that helps users trace and analyze complex objects, providing valuable insights and information about them. Whether you're dealing with intricate data structures or challenging scenarios, Outliner can assist you in gaining a clearer understanding.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Features

-   **Function Tracing**: Trace function calls, returns, and line execution within a Python module.
-   **Data Collection**: Collect detailed data on function executions and execution flow.
-   **Method Tree**: Display a tree of methods used by the object for object behavior exploration.
-   **Easy Integration**: Simple and straightforward integration into your Python projects.
-   **Customizable**: Fine-tune tracing parameters to suit your debugging and exploration

## Instalation
As the library hasn't been released yet, to use it on your machine, you will need to do following steps:

-	**Clone the repository:**
	```
	git clone https://github.com/LucasAndradeDias/outliner.git path/you/want/to/save
	cd path/you/want/to/save
	```

-	**Use pip install:**
	Make sure that path contains the setup.py file
	``` 
	pip install .
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
