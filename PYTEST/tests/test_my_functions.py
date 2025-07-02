# import sys
# import os   
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import time

from Sources import my_functions as mfun

#PYTEST/Sources/my_functions.py


def test_add():
    result = mfun.add(4,7)
    assert result == 119

def test_add_strings():
     result = mfun.add("I like ","Coding")
     assert result == "I like Coding"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
            mfun.divide(10,0)


@pytest.mark.slow #pytest -m slow it will only run below function

def test_slow():
     time.sleep(5)
     result = mfun.divide(10, 2)
     assert result == 5
     
@pytest.mark.skip(reason="This feature is currently broken")

def test_add():
     assert mfun.add(5, 8) == 13

# @pytest.mark.xfail(reason="We know we can't divide anything by zero")     

## chatGPT can be used to create test cases 
