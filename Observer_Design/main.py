from weather_sta import WeatherStation
from observer import Observer
from tv import TVDisplay
from mobile import MobileDisplay

ws = WeatherStation()
observer = Observer()

tv = TVDisplay()
mobile = MobileDisplay()
ws.new_observer(tv)
ws.new_observer(mobile)

ws.update_Temp(100)
tv.display_Temp()