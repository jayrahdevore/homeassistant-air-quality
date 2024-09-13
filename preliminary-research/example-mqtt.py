
# import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.publish as publish
import json

discovery_message = {
  "name": "air quality",
  "state_topic": "air_sensor/current",
  "device_class": "sensor",
  "unique_id": "custom-python-test-1",
  "device": {
    "name": "Test Air Sensor",
    "identifiers": [
      "custom-python"
    ]
  }
}

publish.single("homeassistant/sensor/test/air-sensor/config", json.dumps(discovery_message), hostname="mqtt.internal.devorefamily.xyz")
