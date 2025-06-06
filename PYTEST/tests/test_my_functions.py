import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from Sources import my_functions as mfun

#PYTEST/Sources/my_functions.py


def test_add():
    result = mfun.add(4,7)
    assert result == 119