from Sources import shapes

import pytest


@pytest.mark.parametrize("side_length, expected_area",[(5, 25), (4, 16), (9, 81)])

def test_square_multiple_area(side_length, expected_area):
    assert shapes.square(side_length).area() == expected_area