# Python Example project

Example project where my experiments and Katas live. Also place to explore setup of Python projects. Serves as my own documentation of how to use Python.

## Structure

Following this document to structure the project:
https://docs.python-guide.org/writing/structure/

## Basic Python Unit Test

Docs: https://docs.python.org/3/library/unittest.html

```python
import unittest

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
```

## Python importing

```python
from module_name import file_name

file_name.function_name()
```
