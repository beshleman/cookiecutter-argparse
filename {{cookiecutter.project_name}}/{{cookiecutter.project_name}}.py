#!/usr/bin/env python3
"""
{{cookiecutter.project_name}} - {{cookiecutter.description}}
"""

import argparse

__author__ = "{{cookiecutter.author}}"
__version__ = "0.0.1"
__license__ = "GPLv2"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="{{cookiecutter.description}}")

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
