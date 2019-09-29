
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from numpy_test_module.core import NumpyTestModule

def main():
    numpy_test_module = NumpyTestModule()
    numpy_test_module.print_numpy_examples()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
