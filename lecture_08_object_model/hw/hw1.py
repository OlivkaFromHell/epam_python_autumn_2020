class KeyValueStorage(dict):
    """Key Value Storage class which acts like a dict"""

    def __init__(self, path: str):
        super().__init__()
        with open(path) as f:
            for line in f:
                key, value = line.strip().split('=')

                if key in KeyValueStorage.__dict__ or key in dict.__dict__:
                    continue

                if value.isdigit():
                    value = int(value)

                # name of attribute should be indentifier
                if not key.isidentifier():
                    raise ValueError("Key values should be string type")

                super().__setitem__(key, value)
                setattr(self, key, value)
