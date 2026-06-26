
from chef import Chef
from order import Order
from burger_order import BurgerOrder
from pizza_order import PizzaOrder
from waiter import Waiter

chef = Chef()

burger_order = BurgerOrder(chef)
pizza_order = PizzaOrder(chef)
waiter = Waiter()
waiter.take_order(burger_order)