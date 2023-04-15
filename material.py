class Materials:
    def __init__(self, count, price):
        self.count = count
        self.price = price


class Room:
    def __init__(self, chair, table):
        self.tables = tables
        self.chairs = chairs

    def __repr__(self):
        return f"chairs {self.chairs.count}\n \
               f"tables {self.tables.count}"




tables = Materials(10, 12)
chairs = Materials(20, 5)

room = Room(tables, chairs)
print(room)