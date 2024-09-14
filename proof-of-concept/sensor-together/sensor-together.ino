#include <sps30.h>
#include <Wire.h>
#include "SparkFun_ENS160.h"

// Example arduino sketch, based on 
// https://github.com/Sensirion/embedded-sps/blob/master/sps30-i2c/sps30_example_usage.c


// uncomment the next line to use the serial plotter
// #define PLOTTER_FORMAT
SparkFun_ENS160 myENS; 

int ensStatus; 

void setup() {
  int16_t ret;
  uint8_t auto_clean_days = 4;
  uint32_t auto_clean;

  Serial.begin(9600);
  delay(2000);
	Wire.begin();

	//Serial.begin(115200);

	if( !myENS.begin() )
	{
		Serial.println("Could not communicate with the ENS160, check wiring.");
		while(1);
	}

  Serial.println("Example 1 Basic Example.");

	// Reset the indoor air quality sensor's settings.
	if( myENS.setOperatingMode(SFE_ENS160_RESET) )
		Serial.println("Ready.");

	delay(100);

	// Device needs to be set to idle to apply any settings.
	// myENS.setOperatingMode(SFE_ENS160_IDLE);

	// Set to standard operation
	// Others include SFE_ENS160_DEEP_SLEEP and SFE_ENS160_IDLE
	myENS.setOperatingMode(SFE_ENS160_STANDARD);

	// There are four values here: 
	// 0 - Operating ok: Standard Operation
	// 1 - Warm-up: occurs for 3 minutes after power-on.
	// 2 - Initial Start-up: Occurs for the first hour of operation.
  //												and only once in sensor's lifetime.
	// 3 - No Valid Output
	ensStatus = myENS.getFlags();
	Serial.print("Gas Sensor Status Flag (0 - Standard, 1 - Warm up, 2 - Initial Start Up): ");
	Serial.println(ensStatus);
	

  sensirion_i2c_init();

  while (sps30_probe() != 0) {
    Serial.print("SPS sensor probing failed\n");
    delay(500);
  }

#ifndef PLOTTER_FORMAT
  Serial.print("SPS sensor probing successful\n");
#endif /* PLOTTER_FORMAT */

  ret = sps30_set_fan_auto_cleaning_interval_days(auto_clean_days);
  if (ret) {
    Serial.print("error setting the auto-clean interval: ");
    Serial.println(ret);
  }

  ret = sps30_start_measurement();
  if (ret < 0) {
    Serial.print("error starting measurement\n");
  }

#ifndef PLOTTER_FORMAT
  Serial.print("measurements started\n");
#endif /* PLOTTER_FORMAT */

#ifdef SPS30_LIMITED_I2C_BUFFER_SIZE
  Serial.print("Your Arduino hardware has a limitation that only\n");
  Serial.print("  allows reading the mass concentrations. For more\n");
  Serial.print("  information, please check\n");
  Serial.print("  https://github.com/Sensirion/arduino-sps#esp8266-partial-legacy-support\n");
  Serial.print("\n");
  delay(2000);
#endif

  delay(1000);
}

void loop() {
  struct sps30_measurement m;
  char serial[SPS30_MAX_SERIAL_LEN];
  uint16_t data_ready;
  int16_t ret;

  do {
    ret = sps30_read_data_ready(&data_ready);
    if (ret < 0) {
      Serial.print("error reading data-ready flag: ");
      Serial.println(ret);
    } else if (!data_ready)
      Serial.print("data not ready, no new measurement available\n");
    else
      break;
    delay(100); /* retry in 100ms */
  } while (1);

  ret = sps30_read_measurement(&m);
  Serial.print("{");
  if (ret < 0) {
    // Serial.print("error reading measurement\n");
  } else {
    
    //Serial.print("\"sps30\": {");
    Serial.print("\"pm1\": ");
    Serial.print(m.mc_1p0);
    Serial.print(", \"pm25\": ");
    Serial.print(m.mc_2p5);
    //Serial.print("PM  4.0: ");
    //Serial.println(m.mc_4p0);
    Serial.print(", \"pm10\": ");
    Serial.print(m.mc_10p0);
    //Serial.print("}");



  }

	if( myENS.checkDataStatus() )
	{
    //Serial.print(",\"ens160\": {");
		Serial.print(",\"aqi\": ");
		Serial.print(myENS.getAQI());

		Serial.print(", \"voc\": ");
		Serial.print(myENS.getTVOC());
		//Serial.println("ppb");

		Serial.print(", \"co2\": ");
		Serial.print(myENS.getECO2());
		//Serial.println("ppm");

	Serial.print(", \"status\": ");
    Serial.print(myENS.getFlags());
		//Serial.print("}");


	}

  Serial.println("}");

  delay(120000);
}
