from .advertisement import ImprovAdvertisement
from .protocol import *
from .service import ImprovService

import asyncio
from adafruit_ble import BLERadio
from enum import Enum
import time
import wifi

import logging

logger = logging.getLogger(name=__name__)

ble = BLERadio()

class Improv:
    def __init__(self, redirect_url: str) -> None:
        self.redirect_url = redirect_url
        self.connect_retry_times = 4
        self.protocol = ImprovProtocol(
            wifi_connect_callback=self.__improv_wifi_connect
        )
        pass

    def __improv_wifi_connect(self, ssid: str, passwd: str):
        # much of this is from https://github.com/dotpointer/circuitpython-wifimanager/ 
        # thanks @dotpointer and @tayfunulu
        wifi.radio.enabled = True

        logger.info('Trying to connect to "%s": ' % ssid, end='')
        try:
            wifi.radio.connect(ssid, passwd)
        except Exception as e:
            logger.info('') # close previous line
            logger.exception(e)
            return None # sets last_error to UNABLE_TO_CONNECT
        
        for retry in range(self.connect_retry_times):
            connected = wifi.radio.ap_info is not None
            if connected:
                break
            time.sleep(0.1)
            logger.info('.', end='')

        if not connected:
            logger.warn('Failed to connect to "%s"!' % ssid)
            return None
        else:
            logger.info("Connected!")
            return [self.redirect_url]
    


    