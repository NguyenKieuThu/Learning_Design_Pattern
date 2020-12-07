"""
Building a complex product from many simple sub-component by common way or choosing any component which you want to.
ref: https://www.tutorialspoint.com/design_pattern/builder_pattern.htm
"""
from meal_builder import MealBuilder
from meal import Meal
from burger import ChickenBurger, VegBurger
from drink import Pepsi, Coke


if __name__=="__main__":
    combo = MealBuilder()
    print("===Combo 1===")
    combo_1 = combo.prepare_non_veg_meal()
    combo_1.show_items()
    print("Total cost: ", combo_1.get_cost())
    print("===Combo 2===")
    combo_2 = combo.prepare_combo_burger()
    combo_2.show_items()
    print("Total cost: ", combo_2.get_cost())
    print("===Ordering by customer===")
    ordering = Meal()
    ordering.add_item(ChickenBurger())
    ordering.add_item(VegBurger())
    ordering.add_item(Pepsi())
    ordering.add_item(Pepsi())
    ordering.show_items()
    print("Total cost: ", ordering.get_cost())
