from Sources import shapes

import pytest

@pytest.fixture

def my_rectangle():
    return shapes.rectangle(10, 20)

def test_area(my_rectangle):
    # result = shapes.rectangle(2, 8)
    assert my_rectangle.area() == 10 * 20 # Fixtures
    

def test_perimeter(my_rectangle):
    # result = shapes.rectangle(3,7)
    assert my_rectangle.perimeter() == 2 * (10 + 20)    # Fixtures

# def test_area():
#     result = shapes.rectangle(2, 8)
#     assert result.area() == 2 * 8
    

# def test_perimeter():
#     result = shapes.rectangle(3,7)
#     assert result.perimeter() == 2 * (3 + 7)   