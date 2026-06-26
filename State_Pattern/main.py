
from transport_mode import TransportMode
from transport_service import TransportService
from walk_mode import Walking

walking = Walking()
transport_service = TransportService(walking)

transport_service.eta()
transport_service.directions()

