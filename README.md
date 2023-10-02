# Simple Color Module

The Simple Color Module is a Python package that allows you to easily add color to text in your terminal. It provides both text colors and background colors, along with the ability to specify colors using hexadecimal values. Additionally, it includes a feature to clear the terminal screen.

## Installation

To use the Simple Color Module, follow these installation steps:

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed. This module works with Python 3.

3. Import the `SimpleColor` class from the `simple_color` module in your Python scripts.

## Usage

### Text Colors

You can use the `SimpleColor` class to colorize text using predefined color names. Here's an example:

```python
from simple_color import SimpleColor

text = "Hello, VisualSynced!"

# Using named text color
colored_text_red = SimpleColor.colorize(text, 'red')
print(colored_text_red)
```

### Hexadecimal Colors

You can also specify text colors using hexadecimal values. Here's an example:

```python
from simple_color import SimpleColor

text = "Hello, VisualSynced!"

# Using hex text color
colored_text_hex = SimpleColor.hex_colorize(text, '#FF4500')  # Orange text color
print(colored_text_hex)
```

### Background Colors

You can add background colors to your text as well. For example:

```python
from simple_color import SimpleColor

text = "Hello, VisualSynced!"

# Using text color and background color
colored_text = SimpleColor.colorize(text, 'light_blue', 'bg_red')
print(colored_text)
```

### Clear Terminal

You can clear the terminal screen using the `clear_terminal` method:

```python
from simple_color import SimpleColor

# Clear the terminal screen
SimpleColor.clear_terminal()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- VisuallySynced

Feel free to contribute or report issues on [GitHub](https://github.com/visuallysynced/simple-color-module).

Enjoy using the Simple Color Module for adding color to your Python terminal output and clearing the terminal when needed!
