# Air Quality Sensor for Home Assistant

- [x] Component Testing
  - [x] Get sensor data from SPS30 using example code
  - [x] Get sensor data from ENS160 using example code
  - [x] Publish data to Home Assistant via MQTT
    - [x] Basic device discovery
    - [x] Device discovery w/ description and fields
    - [x] Publish fake data to Home Assistant
- [x] Proof of Concept
  - [x] Combine data from both sensors and send over serial
  - [x] Read data from serial and publish over MQTT
- [ ] Productize using Pico W
  - [ ] Send device discovery and fake data over MQTT
  - [ ] Wire up sensors to Pico W
  - [ ] Retrieve data from SPS30
  - [ ] Retrieve data from ENS160
  - [ ] Design and build enclosure

## LICENSE

Orignal work in this repository is licensed into the public domain. Works taken
from other projects (i.e. example code .ino files) retain their original
licenses and are marked in their header as such.
