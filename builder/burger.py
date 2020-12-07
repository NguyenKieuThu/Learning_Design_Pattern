import packing
import abc
import item


class Burger(item.IItem, abc.ABC):
    def packing(self):
        return packing.Wrapper().pack()


class VegBurger(Burger):
    def name(self):
        return "Veg-Burger"

    def price(self):
        return 10


class ChickenBurger(Burger):
    def name(self):
        return "Chick-Burger"

    def price(self):
        return 20


if __name__=='__main__':
    ver_burger = VegBurger()
    print("Name product: ", ver_burger.name())
    print("Method: ", ver_burger.packing())
    print("Price: ", ver_burger.price())
