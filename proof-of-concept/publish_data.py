# example-mqtt.py
# Written by Jayrah DeVore and released into the public domain

import paho.mqtt.publish as publish
import json

from pydantic import BaseModel
from serial import Serial

device = Serial("/dev/ttyUSB0", 9600)

class Message(BaseModel):
    aqi: int
    voc: float
    co2: float
    pm1: float
    pm25: float
    pm10: float

state_topic = "homeassistant/sensor/sensorTestAirQuality/state"

# message = {
#     "aqi": 1,
#     "voc": 0.0,
#     "co2": 400,
#     "pm1": 0.5,
#     "pm25": 0.5,
#     "pm10": 0.5,
# }

while True:
    line = device.readline()
    print(line)
    try:
        msg = Message.parse_raw(line)
        publish.single(
            state_topic,
            msg.model_dump_json(),
            hostname="mqtt.internal.devorefamily.xyz",
        )
    except Exception as e:
        print(f"An error occured: {e}")

#
# We have a few SensorDeviceClasses we'll be uploading...
# From the ENS160
# - AQI (Air quality index)
# - VOLATILE_ORGANIC_COMPOUNDS (VOC)
# - CO2
# From the SPS30
# - PM1 (PM1.0)
# - PM25 (PM2.5)
# - PM10 (PM10)



