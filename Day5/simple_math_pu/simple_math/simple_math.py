"""
A collection of simple math operations
"""

def simple_add(a,b):
    """Addition of two values. Commutative

    Parameters
    ----------
    a : int or float
        First value for addition.
    b : int or float
        Second value for addition.

    Returns
    -------
    int or float
        Return the sum of value a and b.

    """
    return a+b

def simple_sub(a,b):
    """Substraction of two values. Non commutative

    Parameters
    ----------
    a : int or float
        Value to be substracted from.
    b : int or float
        Value that is substracting.

    Returns
    -------
    int ot float
        Return substraction of value b from a.

    """
    return a-b

def simple_mult(a,b):
    """ Multiplication of two values. Commutative

    Parameters
    ----------
    a : int or float
        First value for multiplication
    b : int or float
        Second value for multiplication

    Returns
    -------
    int or float
        Return multiplication of value a and b.

    """
    
    return a*b

def simple_div(a,b):
    """ Multiplication of two values. Non commutative

    Parameters
    ----------
    a : int or float
        Value to be divided
    b : int or float
        Value that divide value a

    Returns
    -------
    float
        Return division of value a by b.

    """    
    return a/b

def poly_first(x, a0, a1):
    """Compute polynomial of first order 
    

    Parameters
    ----------
    x : int or float
        Value to be squared.
    a0 : int or float
        Constant factor.
    a1 : int or float
        Scaling factor of the value x.

    Returns
    -------
    float
        Return first order polynomial of the three input values.

    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Compute polynomial of second order 
    

    Parameters
    ----------
    x : int or float
        Value to be squared.
    a0 : int or float
        Constant factor.
    a1 : int or float
        Scaling factor of the value x.
    a2 : int or float
        Scaling factor of the squared value x.        

    Returns
    -------
    float
        Return second order polynomial of the four input values.

    """
     
    
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
