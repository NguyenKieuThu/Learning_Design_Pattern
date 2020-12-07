import packing
import abc
import item


class ColdDrink(item.IItem, abc.ABC):
    def packing(self):
        return packing.Bottle().pack()


class Pepsi(ColdDrink):
    def name(self):
        return "Pepsi"

    def price(self):
        return 5


class Coke(ColdDrink):
    def name(self):
        return "Coke"

    def price(self):
        return 4


if __name__=='__main__':
    pep = Pepsi()
    print("Name product: ", pep.name())
    print("Method: ", pep.packing().pack())
    print("Price: ", pep.price())
