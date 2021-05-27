# Testing python code with built in unittest lib

### Prerequisites
None

The built in unittest lib is a great way of testing your python code with unit tests.
However, pytest might be even better since with that you can select which tests to
run by decorators and continue running where you stopped etc. But pytest requires
intallation of pytest.

### Structure
It is good practise to always name your files, that contains your test cases, starting
with "test", like testMyClass.py or test_my_class.py. If you do so the unittest can
automatically find test files that is placed in subfolders, like in a "tests" subfolder.

Lets say you have a structure like this:

project/
|
|-- src/
|   |-- my_program.py
|   |-- __init__.py
|
|-- tests/
|   |-- test_my_program.py
|   |-- prov_my_program.py
|   |-- __init__.py
|
|-- testing_my_program.py
|-- do_test_my_program.py

my_program.py contains your program code. All other files contains unit tests.
In this case you would be able to execute testing_my_program.py and do_test_my_program.py
by just starting them like ./do_test_my_program.py.
But the unit tests in the tests folder cannot be executed like that since they are not
able to include the my_program.py file because it is not in a subdirectory under the folder
where the test file is located.
The trick to execute test files in a subdir is to execute them with the command:
```python -m unittest discover -s tests -t .```
The "discover" part will find all files starting with "test" and the -s will tell it to
look for test files in the tests folder. -t will tell in which folder the test shall be
executed in (I have not really made this work for other than .).

### Source
https://realpython.com/python-testing/

