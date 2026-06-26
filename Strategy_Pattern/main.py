
from discount_service import DiscountService
from discount_strategy import DiscountStrategy
from diwali import DiwaliOffer
from holi import HoliOffer


diwali = DiwaliOffer()
holi = HoliOffer()
discount_service = DiscountService(200,holi)


discount_service.process()