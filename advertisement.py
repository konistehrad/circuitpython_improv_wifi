from .protocol import *
from .service import ImprovService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement, ServiceData

class ImprovServiceData(ServiceData):
    def __init__(self):
        super().__init__(ImprovService)
    
    def __get__(self, obj, cls):
        if obj is None:
            return self
        return super().__get__(obj, cls)[1:]
    
    def __set__(self, obj, value):
        # ServiceData requires a bytearray.
        return super().__set__(obj, bytearray(obj.frame_type) + value)
    
class ImprovAdvertisement(ProvideServicesAdvertisement):
    service_data = ImprovServiceData()
    
    def __init__(self, service: ImprovService):
        super().__init__(service)
        self.service_data = bytearray([service.status, 0])



