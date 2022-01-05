import pytest
from hw.hw2 import Suppresor, suppresor


def test_positive_case_class_1():
    with Suppresor(IndexError):
        [][2]


def test_positive_case_class_2():
    with Suppresor(ZeroDivisionError):
        1 / 0


def test_negative_case_class_1():
    with pytest.raises(TypeError):
        with Suppresor(IndexError):
            []['year']


def test_negative_case_class_2():
    with pytest.raises(AttributeError):
        with Suppresor(ZeroDivisionError):
            object.non_existing_attribute


def test_positive_case_generator_1():
    with suppresor(IndexError):
        [][2]


def test_positive_case_generator_2():
    with suppresor(ZeroDivisionError):
        1 / 0


def test_negative_case_senerator_1():
    with pytest.raises(AttributeError):
        with Suppresor(ZeroDivisionError):
            object.non_existing_attribute


def test_negative_case_senerator_2():
    with pytest.raises(TypeError):
        with Suppresor(IndexError):
            []['year']
