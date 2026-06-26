from discount_strategy import DiscountStrategy

class DiwaliOffer(DiscountStrategy):
     
          
     def calculate_discount(self,price):
          self.__amount = (price*9)/10
          print(f"Price after applying the Holi Offer : {self.__amount}")