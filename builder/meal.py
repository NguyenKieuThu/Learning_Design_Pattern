class Meal:
    def __init__(self):
        self._items = []
        self._cost = 0

    def add_item(self, item):
        self._items.append(item)
        self._cost += item.price()

    def get_cost(self):
        return self._cost

    def show_items(self):
        for index, item in enumerate(self._items):
            print("{} - {}, {} with {} vnd".format(index+1, item.name(), item.packing(), item.price()))


if __name__=="__main__":
    from burger import VegBurger, ChickenBurger
    from drink import Pepsi, Coke
    list_order = Meal()
    list_order.add_item(VegBurger())
    list_order.add_item(Coke())
    list_order.show_items()
    print("Total cost: ", list_order.get_cost())

