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
device = {"identifiers": ["household-airq"]}

discovery_messages = {
    "sensorTestAQI": {
        "device_class": "aqi",
        "state_topic": state_topic,
        "unit_of_measurement": None,
        "value_template":"{{ value_json.aqi}}",
        "unique_id": "aqi01",
        "device": device | {"name": "test-air-quality"},  # add to first message
    },
    "sensorTestVOC": {
        "device_class": "volatile_organic_compounds",
        "state_topic": state_topic,
        "unit_of_measurement": "µg/m³",
        "value_template":"{{ value_json.voc}}",
        "unique_id": "voc01",
        "device": device,
    },
    "sensorTestCo2": {
        "device_class": "carbon_dioxide",
        "state_topic": state_topic,
        "unit_of_measurement": "ppm",
        "value_template":"{{ value_json.co2}}",
        "unique_id": "co201",
        "device": device,
    },
    "sensorTestPM1": {
        "device_class": "pm1",
        "state_topic": state_topic,
        "unit_of_measurement": "µg/m³",
        "value_template":"{{ value_json.pm1}}",
        "unique_id": "pm101",
        "device": device,
    },
    "sensorTestPM25": {
        "device_class": "pm25",
        "state_topic": state_topic,
        "unit_of_measurement": "µg/m³",
        "value_template":"{{ value_json.pm25}}",
        "unique_id": "pm2501",
        "device": device,
    },
    "sensorTestPM10": {
        "device_class": "pm10",
        "state_topic": state_topic,
        "unit_of_measurement": "µg/m³",
        "value_template":"{{ value_json.pm10}}",
        "unique_id": "pm1001",
        "device": device,
    },
}

# discovery_message = {
#   "name": "air quality",
#   "state_topic": "air_sensor/current",
#   "device_class": "sensor",
#   "unique_id": "custom-python-test-1",
#   "device": {
#     "name": "Test Air Sensor",
#     "identifiers": [
#       "custom-python"
#     ]
#   }
# }
for sensorName, message in discovery_messages.items():
    publish.single(
        f"homeassistant/sensor/{sensorName}/config",
        json.dumps(message),
        hostname="mqtt.internal.devorefamily.xyz",
    )
