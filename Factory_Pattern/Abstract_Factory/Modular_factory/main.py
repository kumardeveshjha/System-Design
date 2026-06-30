from cusine_factory import CusineFactory
from north_indian import NorthIndian

class RestaurantService:
     def __init__(self,cusine_type: CusineFactory):
          self.__cusine = cusine_type
          
     def prepare_cusine(self):
          starter = self.__cusine.starter()
          main_course = self.__cusine.main_course()
          dessart = self.__cusine.dessart()
          
          starter.prepare_food()
          main_course.prepare_food()
          dessart.prepare_food()
          
north_indian = NorthIndian()

rest_service = RestaurantService(north_indian)
rest_service.prepare_cusine()