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
    class NewCls:
        counter = defaultdict(int)

        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)
            NewCls.counter[self.__class__.__name__] += 1

        @classmethod
        def get_created_instances(cls):
            return NewCls.counter[cls.__name__]

        @classmethod
        def reset_instances_counter(cls):
            try:
                return NewCls.counter[cls.__name__]
            finally:
                NewCls.counter[cls.__name__] = 0

    return NewCls


@instances_counter
class User:
    pass


class SubUser(User):
    pass


class SubSubUser(SubUser):
    counter = 1

    def __init__(self):
        super().__init__()
        self.counter = 2


if __name__ == '__main__':
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    sub_user = SubUser()
    sub_sub_user = SubSubUser()
    print(user.get_created_instances())
    print(sub_user.get_created_instances())
    print(User.get_created_instances())  # 0
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())  # 0
    print('subsub', sub_sub_user.get_created_instances())
    print(user.counter[User.__name__])
