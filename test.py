import pytest
import vector as vec

a = vec.Vector([1, 2, 3])
b = vec.Vector([4, 5, 6])
c = vec.Vector([7, 8, 9, 0])
a_plus_b = vec.Vector([5, 7, 9])

### __init__
def test_correct_length():
    assert a.len == 3

def test_correct_content():
    assert a.content == [1, 2, 3]

### get_element
def test_get_first_element():
    assert a.get_element(1) == 1

def test_get_last_element():
    assert a.get_element(3) == 3

def test_get_lower_element():
    with pytest.raises(Exception):
        a.get_element(-2)

def test_get_higher_element():
    with pytest.raises(Exception):
        a.get_element(5)

### sum_vectors
def test_correct_sum():
    a_sum_b = a.sum_vectors(b)
    assert a_sum_b.content == a_plus_b.content

def test_sum_different_lengths():
    with pytest.raises(Exception):
        a.sum_vectors(c)

### subtract_vectors
def test_correct_subtraction():
    a_minus_b = a_plus_b.subtract_vectors(b)
    assert a_minus_b.content == a.content

def test_subtract_different_lengths():
    with pytest.raises(Exception):
        a.subtract_vectors(c)

### multiply_vectors
def test_correct_multiplication():
    a_times_b = a.multiply_vectors(b)
    assert a_times_b == 32

def test_subtract_different_lengths():
    with pytest.raises(Exception):
        a.multiply_vectors(c)