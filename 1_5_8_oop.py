class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{x.name}: {x.price}" for x in self.goods]


class Table:
    def __init__(self, name, price):







gd=