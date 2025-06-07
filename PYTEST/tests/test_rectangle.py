from Sources import shapes

def test_area():
    result = shapes.rectangle(2, 8)
    assert result.area() == 2 * 8
    

def test_perimeter():
    result = shapes.rectangle(3,7)
    assert result.perimeter() == 2 * (3 + 7)    
