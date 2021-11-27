# I decided to write a code that generates data filtering object from a list of keyword parameters:


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]


# positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
# positive_even.apply(range(100))


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = [lambda item, key=key, value=value: item.get(key, False) == value for key, value in
                    keywords.items()]

    return Filter(*filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly",
    }
]

keys = {'name': 'polly', 'type': 'person'}

# should return only second entry from the list
a = make_filter(**keys).apply(sample_data)
print(a)

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
