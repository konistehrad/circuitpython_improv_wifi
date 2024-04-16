from .protocol import *

from adafruit_ble.services import Service
from adafruit_ble.characteristics import Characteristic
from adafruit_ble.characteristics.stream import StreamIn
from adafruit_ble.characteristics.int import Uint8Characteristic
from adafruit_ble.uuid import VendorUUID

import logging

logger = logging.getLogger(name=__name__)

class ImprovService(Service):
    """ Service to manage Improv interaction """
    uuid = VendorUUID(ImprovUUID.SERVICE_UUID)
    status = Uint8Characteristic(
        uuid=ImprovUUID.STATUS_UUID,
        properties=(Characteristic.READ | Characteristic.NOTIFY),
    )
    error_state = Uint8Characteristic(
        uuid=ImprovUUID.ERROR_UUID,
        properties=(Characteristic.READ | Characteristic.NOTIFY),
    )
    rpc_command = StreamIn(
        uuid=ImprovUUID.RPC_COMMAND_UUID,
        properties=(Characteristic.WRITE | Characteristic.WRITE_NO_RESPONSE),
    )
    rpc_result = Uint8Characteristic(
        uuid=ImprovUUID.RPC_RESULT_UUID,
        properties=(Characteristic.READ | Characteristic.NOTIFY),
    )
    capabilities = Uint8Characteristic(
        uuid=ImprovUUID.CAPABILITIES_UUID,
        properties=(Characteristic.READ),
    )


    


    


