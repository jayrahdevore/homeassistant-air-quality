# Air Quality Sensor for Home Assistant

- [ ] Component Testing
  - [x] Get sensor data from SPS30 using example code
  - [x] Get sensor data from ENS160 using example code
  - [ ] Publish data to Home Assistant via MQTT
    - [ ] Basic device discovery
    - [ ] Device discovery w/ description and fields
    - [ ] Publish fake data to Home Assistant
- [ ] Proof of Concept
  - [ ] Combine data from both sensors and send over serial
  - [ ] Read data from serial and publish over MQTT
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
