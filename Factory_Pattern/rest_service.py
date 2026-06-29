from food_factory import FoodFactroy

class RestaurantService:
     
     def food_order(self,order_food:str):
          food =  FoodFactroy.prepare_food(order_food)
          if food == None:
               return "We are sorry we can not serve that to you"
          return food

restaurant_service = RestaurantService()
restaurant_service.food_order("dosa")
restaurant_service.food_order("pasta")