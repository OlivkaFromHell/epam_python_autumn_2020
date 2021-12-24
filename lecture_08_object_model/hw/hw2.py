import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.table_name = table_name

        conn = sqlite3.connect(database_name)
        self.cursor = conn.cursor()

        # get table column names to use them as dict keys
        self.cursor.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{table_name}')")
        self.columns = []
        for column in self.cursor.fetchall():
            self.columns.append(column[0])

    def __contains__(self, item):
        for row in self:
            values = list(row.values())
            if item in values:
                return True
        return False

    def __len__(self):
        self.cursor.execute(f"SELECT count(*) FROM {self.table_name}")
        data = self.cursor.fetchone()[0]
        return data

    def __iter__(self):
        for row in self.cursor.execute(f'SELECT * FROM {self.table_name}'):
            response = {}
            for key, value in zip(self.columns, row):
                response[key] = value
            yield response

    def __getitem__(self, item):
        if isinstance(item, str):
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE name = '{item}'")
            response = {}
            row = self.cursor.fetchone()

            for key, value in zip(self.columns, row):
                response[key] = value
            return response

        raise KeyError('item object should be string')


if __name__ == '__main__':
    example = TableData('example.sqlite', 'books')

    #
    # print(len(example))

    # for i in example:
    #     print(i['author'])

    print('1984' in example)

    # print(example['Farenheit 451'])
