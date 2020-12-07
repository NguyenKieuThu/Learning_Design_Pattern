"""
It plays with Director role.
Define some menu common or combo.
But the client can choose any products to build a special menu by their favorite. Example at the end of the meal.py file.
"""
import meal
from burger import VegBurger, ChickenBurger
from drink import Pepsi, Coke


class MealBuilder:
    @staticmethod
    def prepare_veg_meal():
        orders = meal.Meal()
        orders.add_item(VegBurger())
        orders.add_item(Pepsi())
        return orders

    @staticmethod
    def prepare_non_veg_meal():
        orders = meal.Meal()
        orders.add_item(ChickenBurger())
        orders.add_item(Coke())
        return orders

    @staticmethod
    def prepare_combo_burger():
        orders = meal.Meal()
        orders.add_item(ChickenBurger())
        orders.add_item(VegBurger())
        return orders


