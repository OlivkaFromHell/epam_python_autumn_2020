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
            NewCls.counter += 1
            self._obj = cls(*args, **kwargs)

        @staticmethod
        def get_created_instances():
            return NewCls.counter

        @staticmethod
        def reset_instances_counter():
            old_value = NewCls.counter
            NewCls.counter = 0
            return old_value

    return NewCls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())
