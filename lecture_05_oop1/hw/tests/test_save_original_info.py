from hw.save_original_info import wraps


def test_doc_name():
    def print_result(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Function-wrapper which print result of an original function"""
            result = func(*args, **kwargs)
            return result

        return wrapper

    @print_result
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return sum(args)

    assert custom_sum.__doc__ == """This function can sum any objects which have __add___"""
    assert custom_sum.__name__ == 'custom_sum'


def test_original_func():
    def print_result(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Function-wrapper which print result of an original function"""
            result = func(*args, **kwargs) + 1
            return result

        return wrapper

    @print_result
    def custom_sum(*args):
        """This function can sum any objects which have __add___"""
        return sum(args)

    without_add_1 = custom_sum.__original_func
    assert without_add_1(1, 2, 3, 4) + 1 == custom_sum(1, 2, 3, 4)
