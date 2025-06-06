import pytest
import math

import Sources.shapes as shapes

class TestCircles:


    def setup_method(self, method):
        print(f"************** This fx will run before each and every test {method} ***********")
        self.circle = shapes.circle(10)


    def teardown_method(self, method):
        print(f"************* This fx will run after each and every test {method} ************") # here method means tests

        del self.circle


    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_one(self):
        
        assert True

        # result =  shapes.circle(7)

        # assert 