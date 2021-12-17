import pytest
from hw.counter import instances_counter


@pytest.fixture
def data():
    @instances_counter
    class User:
        @staticmethod
        def throw_one():
            return 1

    class SubUser(User):
        def __init__(self):
            super().__init__()

        @staticmethod
        def throw_two():
            return 2

    class SubSubUser(SubUser):
        counter = 1

        def __init__(self):
            super().__init__()
            self.counter = 2

    @instances_counter
    class Admin:
        pass

    class Moderator(Admin):
        def __init__(self):
            super().__init__()
            self.users = []

    class Advisor(User, Moderator):
        counter = 1

        def __init__(self):
            super().__init__()
            self.counter = 2

    return User, SubUser, SubSubUser, Admin, Moderator, Advisor


def test_class_get_created_instances(data):
    user_class, _, _, _, _, _ = data
    assert user_class.get_created_instances() == 0


def test_subclass_get_created_instances(data):
    _, sub_user_class, _, _, _, _ = data
    assert sub_user_class.get_created_instances() == 0


def test_advisor_get_created_instances(data):
    _, _, _, _, _, advisor_class = data
    assert advisor_class.get_created_instances() == 0


def test_instance_get_created_instances(data):
    user_class, _, _, _, _, _ = data
    user, _, _ = user_class(), user_class(), user_class()
    assert user.get_created_instances() == 3


def test_user_instance_get_created_instances(data):
    user_class, _, _, _, _, _ = data
    user, _, _ = user_class(), user_class(), user_class()
    assert user.get_created_instances() == 3


def test_subclass_instance_get_created_instances(data):
    user_class, sub_user_class, _, _, _, _ = data
    _, _, _ = user_class(), user_class(), user_class()
    sub_user = sub_user_class()
    assert sub_user.get_created_instances() == 1


def test_advisor_instance_get_created_instances(data):
    user_class, sub_user_class, _, _, _, advisor_class = data
    user, _, _ = user_class(), user_class(), user_class()
    _ = sub_user_class()
    advisor, _ = advisor_class(), user_class()
    assert advisor.get_created_instances() == 1
    assert user.get_created_instances() == 4


def test_user_instance_reset_instances_counter(data):
    user_class, _, _, _, _, _ = data
    user, _, _ = user_class(), user_class(), user_class()
    assert user.reset_instances_counter() == 3
    assert user.get_created_instances() == 0


def test_subuser_instance_reset_instances_counter(data):
    user_class, sub_user_class, _, _, _, _ = data
    _, _, _ = user_class(), user_class(), user_class()
    sub_user = sub_user_class()
    assert sub_user.reset_instances_counter() == 1
    assert sub_user.get_created_instances() == 0


def test_advisor_instance_reset_instances_counter(data):
    user_class, sub_user_class, _, _, _, advisor_class = data
    _, _, _ = user_class(), user_class(), user_class()
    _ = sub_user_class()
    advisor, _ = advisor_class(), user_class()
    assert advisor.reset_instances_counter() == 1
    assert advisor.get_created_instances() == 0


def test_methods_acces(data):
    user_class, _, _, _, _, _ = data

    assert user_class.throw_one() == 1


def test_methods_acces_child_class(data):
    _, sub_user_class, _, _, _, _ = data
    assert sub_user_class.throw_one() == 1


def test_methods_acces_child_class_derive_method(data):
    _, sub_user_class, _, _, _, _ = data
    assert sub_user_class.throw_two() == 2
