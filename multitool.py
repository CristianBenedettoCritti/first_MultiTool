#!/usr/bin/env python3
"""
First MultiTool - A simple command-line multi-tool application
Provides various utility functions in one convenient tool
"""

import sys
import argparse


def text_upper(text):
    """Convert text to uppercase"""
    return text.upper()


def text_lower(text):
    """Convert text to lowercase"""
    return text.lower()


def text_reverse(text):
    """Reverse text"""
    return text[::-1]


def calculate(operation, num1, num2):
    """Perform basic calculations"""
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }
    
    if operation not in operations:
        return f"Error: Unknown operation '{operation}'"
    
    try:
        result = operations[operation](float(num1), float(num2))
        return result
    except ValueError:
        return "Error: Invalid numbers provided"


def count_words(text):
    """Count words in text"""
    words = text.split()
    return len(words)


def count_chars(text):
    """Count characters in text"""
    return len(text)


def main():
    """Main function to handle command-line interface"""
    parser = argparse.ArgumentParser(
        description='First MultiTool - Your all-in-one utility tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s text upper "hello world"
  %(prog)s text lower "HELLO WORLD"
  %(prog)s text reverse "hello"
  %(prog)s calc add 5 3
  %(prog)s calc multiply 4 7
  %(prog)s count words "hello world from multitool"
  %(prog)s count chars "hello"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Text operations
    text_parser = subparsers.add_parser('text', help='Text manipulation tools')
    text_parser.add_argument('operation', choices=['upper', 'lower', 'reverse'],
                            help='Text operation to perform')
    text_parser.add_argument('text', help='Text to process')
    
    # Calculator
    calc_parser = subparsers.add_parser('calc', help='Basic calculator')
    calc_parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'],
                            help='Mathematical operation')
    calc_parser.add_argument('num1', help='First number')
    calc_parser.add_argument('num2', help='Second number')
    
    # Count operations
    count_parser = subparsers.add_parser('count', help='Counting tools')
    count_parser.add_argument('operation', choices=['words', 'chars'],
                             help='What to count')
    count_parser.add_argument('text', help='Text to analyze')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Execute the appropriate command
    if args.command == 'text':
        if args.operation == 'upper':
            result = text_upper(args.text)
        elif args.operation == 'lower':
            result = text_lower(args.text)
        elif args.operation == 'reverse':
            result = text_reverse(args.text)
        print(result)
    
    elif args.command == 'calc':
        result = calculate(args.operation, args.num1, args.num2)
        print(result)
    
    elif args.command == 'count':
        if args.operation == 'words':
            result = count_words(args.text)
        elif args.operation == 'chars':
            result = count_chars(args.text)
        print(f"{result}")


if __name__ == '__main__':
    main()
