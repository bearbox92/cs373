# -----------
# Mon, 11 Sep
# -----------

"""
Piazza
    weekly blog
    pay attention to my responses

Docker
    autopep8
    cmake
    vim

Collatz
    type annotations
    you're not required to use

unit testing with Python's unittest
coverage
Collatz optimizations

exercise
    demonstrate that bad tests can hide bad code

user errors
    exceptions

IsPrime
    1. identify the bad tests
    2. fix the tests
    3. identify the bad code
    4. fix the code
"""

def f (..., e2) :
    ...
    assert <something not wrong>
    if (<something wrong>) :
        e2[0] = <special value>
        return ...
    ...

def g (...) :
    ...
    e = [0]
    x = f(..., e)
    if (e[0] == <special value>) :
        <do something>
    ...

...
...g(...)...
...

"""
three avenues of communication
    1. return
    2. globals
    3. parameters

assertions: because they'll halt the code
returns, globals, parameters: they can be ignored
"""

def f (...) :
    ...
    if (<something wrong>) :
        raise Child_of_E(...)
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except (Child_of_E as e) :
        <do something>
        raise E(...) # handled in next higher try block
    except (E as e) :
        <do something>
    else : # only for (1)
        ...
    finally : # always
    ...
"""
1. no exception was raised
2. exception was raised and handled
3. exception was raised and not handled
"""
...
...g(...)...
...

















