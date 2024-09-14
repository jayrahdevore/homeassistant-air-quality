# example-mqtt.py
# Written by Jayrah DeVore and released into the public domain

import paho.mqtt.publish as publish
import json

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

# We need a discovery message for each sensor

state_topic = "homeassistant/sensor/sensorTestAirQuality/state"

message = {
    "aqi": 1,
    "volatile_organic_compounds": 0.0,
    "carbon_dioxide": 400,
    "pm1": 0.5,
    "pm25": 0.5,
    "pm10": 0.5,
}
publish.single(
    state_topic,
    json.dumps(message),
    hostname="mqtt.internal.devorefamily.xyz",
)
