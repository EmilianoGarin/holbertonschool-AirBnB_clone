# AirBnb Clone

First part of the AirBnb Clone project, in this part the console is made to
manage the objects

# Command list

- Create - Creates a new instance
- Show - Prints the string representation of an instance
- Destroy - Deletes an instance based on the class and id
- All - Prints all string represntation of all instances
- Update - Updates an instance based on class and id
- Help - shows commands
- Quit - Exit the console

# Installing

> git clone https://github.com/EmilianoGarin/holbertonschool-AirBnB_clone.git

# Use

The console can be used in interactive and not interactive mode

### Interactive mode

First you start the console: 
>./console.py

Then you can use the commands

### Non Interactive mode

> cat test
all
>cat test | ./console.py

# Examples of commands:

    to create:
        create <object class>

    to show:
        show <object class> <object id>

    to destroy:
        destroy <object class> <object id>

    to all:
        all                 (prints all the elemnts)
        all <object class>  (prints all the elemnts of object class)

    to update:
        update <object class> <object id> <key> <value>

# Resources

- cmd module
- packages concept page
- uuid module
- datetime
- unittest module
- args/kwargs
- Python test cheatsheet

# Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
