#  This is the bad example for the offfers for the discount in the e-commerce 

from regex import D


class Offers:
     
     def __init__(self,price):
               self.price = price
                        
     def applied_offers(self,discount: str):
          
          if discount == "first_time":
               discounted_price = (self.price * 9)/10 
               return discounted_price
          elif discount == "diwali":
               discounted_price = (self.price * 7)/10 
               return discounted_price
          elif discount == "holi":
               discounted_price = (self.price * 8)/10 
               return discounted_price
          elif discount == "rakshabandhan":
               discounted_price = (self.price * 8.5)/10 
               return discounted_price
          else:
               return "Koi Choot nahi dalle"
          

my_offer = Offers(200)

print(my_offer.applied_offers("diwali"))
