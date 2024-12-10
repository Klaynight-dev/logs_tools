# logs_tools

Here you will find useful logging tools for your Python applications.

## Description

This project provides logging tools for Python applications. It is designed to be simple to use and integrate into your existing Python projects.

## Installation

To install this project, use the following command:

```sh
git clone https://github.com/Klaynight-dev/logs_tools_python.git
```

Then, navigate to the project directory and install the required dependencies:

```sh
cd logs_tools
pip install -r requirements.txt
```

## Usage

```python
from logs_tools import logger

# Example usage
# -> Success
log_action("This is a test", True, None, True)

# -> Error
log_action("This is a test", False, "This is an error", True)
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Authors

- [Klaynight-dev](https://github.com/Klaynight-dev)

## Acknowledgments

Thank you to all the contributors and users of this project.
