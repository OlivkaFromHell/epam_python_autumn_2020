import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.table_name = table_name

        self._conn = sqlite3.connect(database_name)
        self._cursor = self._conn.cursor()

        # get table column names to use them as dict keys
        self._cursor.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{self.table_name}')")
        columns = []
        for column in self.cursor.fetchall():
            columns.append(column[0])
        self.columns = columns

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def close(self):
        self.connection.close()

    def __contains__(self, item):
        for row in self:
            values = list(row.values())
            if item in values:
                return True
        return False

    def __len__(self):
        self._cursor.execute(f"SELECT count(*) FROM {self.table_name}")
        data = self.cursor.fetchone()[0]
        return data

    def __iter__(self):
        for row in self._cursor.execute(f'SELECT * FROM {self.table_name}'):
            response = {}
            for key, value in zip(self.columns, row):
                response[key] = value
            yield response

    def __getitem__(self, item):

        if isinstance(item, str):
            self._cursor.execute(f"SELECT * FROM {self.table_name} WHERE name=:name", f'{{name:{item}}}')
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
