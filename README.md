# first_MultiTool

Hello there, this is my first MultiTool! 🛠️

A simple yet powerful command-line multi-tool application that provides various utility functions in one convenient tool.

## Features

- **Text Manipulation**: Convert text to uppercase, lowercase, or reverse it
- **Calculator**: Perform basic arithmetic operations (add, subtract, multiply, divide)
- **Text Analysis**: Count words and characters in text

## Installation

No installation required! Just make sure you have Python 3 installed on your system.

```bash
# Make the script executable
chmod +x multitool.py
```

## Usage

### Text Operations

```bash
# Convert to uppercase
python3 multitool.py text upper "hello world"

# Convert to lowercase
python3 multitool.py text lower "HELLO WORLD"

# Reverse text
python3 multitool.py text reverse "hello"
```

### Calculator

```bash
# Addition
python3 multitool.py calc add 5 3

# Subtraction
python3 multitool.py calc subtract 10 4

# Multiplication
python3 multitool.py calc multiply 4 7

# Division
python3 multitool.py calc divide 20 5
```

### Counting Tools

```bash
# Count words
python3 multitool.py count words "hello world from multitool"

# Count characters
python3 multitool.py count chars "hello"
```

## Help

To see all available commands and options:

```bash
python3 multitool.py --help
python3 multitool.py text --help
python3 multitool.py calc --help
python3 multitool.py count --help
```

## Requirements

- Python 3.6 or higher

## License

Open source - feel free to use and modify!