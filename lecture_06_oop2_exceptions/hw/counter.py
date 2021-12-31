"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
from collections import defaultdict


def instances_counter(cls):
    class NewCls(cls):
        counter = defaultdict(int)

        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)
            NewCls.counter[self.__class__.__name__] += 1

        @classmethod
        def get_created_instances(cls):
            return NewCls.counter[cls.__name__]

        @classmethod
        def reset_instances_counter(cls):
            old_counter = NewCls.counter[cls.__name__]
            NewCls.counter[cls.__name__] = 0
            return old_counter

    return NewCls


@instances_counter
class User:
    user_data = 'nothing'

    @staticmethod
    def throw_one():
        return 1


class SubUser(User):
    def __init__(self):
        super().__init__()

    @staticmethod
    def throw_two():
        return 2


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    sub_user = SubUser()
    print(SubUser.get_created_instances())
    print(User.user_data)
    print('throw 2', SubUser.throw_one())
    print(User.get_created_instances())  # 0
