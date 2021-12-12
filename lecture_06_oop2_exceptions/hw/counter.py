"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    class NewCls:
        counter = 0

        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)
            NewCls.counter += 1
            self._obj.counter = NewCls.counter

        @classmethod
        def get_created_instances(cls):
            return cls.counter

        @classmethod
        def reset_instances_counter(cls):
            try:
                return cls.counter
            finally:
                cls.counter = 0

        def __getattribute__(self, item):
            try:
                print('smth')
                x = super().__getattribute__(item)
            except AttributeError:
                print('error')
                return self._obj.__getattribute__(item)
            finally:
                return x

    return NewCls


@instances_counter
class User:
    pass


class SubUser(User):
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    sub_user = SubUser()
    print(SubUser.get_created_instances())
    print(sub_user.get_created_instances())
    print(user.counter)
    print(sub_user.counter)
    # print(User.get_created_instances())  # 0

    # print(sub_user.get_created_instances())
    # print(user.get_created_instances())  # 3
    # print(user.reset_instances_counter())  # 3
    # print(user.get_created_instances())
