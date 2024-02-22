import simple_math


a = 10
b = 5

def test_math():
    assert simple_math.simple_add(a,b) == 15
    assert simple_math.simple_sub(a,b) == 5
    assert simple_math.simple_mult(a,b) == 50
    assert simple_math.simple_div(a,b) == 2
    assert simple_math.poly_first(2, a,b) == 20
    assert simple_math.poly_second(2,a,b,4) == 36