from discount_strategy import DiscountStrategy

class DiscountService:
     
     def __init__(self,price, discount_strategy:DiscountStrategy):
          self.__price = price
          self.__discounted_strategy = discount_strategy
          
     def set_strategy(self,new_discount_strategy: DiscountStrategy):
          self.__discounted_strategy = new_discount_strategy
             
     def process(self):
           self.__discounted_strategy.calculate_discount(self.__price)
          