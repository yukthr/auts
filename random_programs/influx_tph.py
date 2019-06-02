#!/usr/bin/env python
import bme680
import time

from influxdb import InfluxDBClient
client = InfluxDBClient(host='192.168.0.137', port=8086)
client.switch_database('mydb')


print("""Display Temperature, Pressure and Humidity

If you don't need gas readings, then you can read temperature,
pressure and humidity quickly.

Press Ctrl+C to exit

""")

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)



class update_influx:

    def __init__(self, temperature, pressure, humidity):

        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

    def dynamic_json_update_influx(self):
        json_data = [
            {
                "measurement": "atmos",
                "tags": {
                    "temp" : "value",
                    "press" : "value",
                    "humid" : "value"
                },
                "fields": {
                    "temp" : "{}".format(self.temperature),
                    "press" : "{}".format(self.pressure),
                    "humid" : "{}".format(self.humidity)
                }
            }
        ]

        client.write_points(json_data)


while True:
    try:
        while True:
            if sensor.get_sensor_data():
                    temperature = "%f"%sensor.data.temperature
                    pressure = "%2f"%sensor.data.pressure
                    humidity = "%3f"%sensor.data.humidity
                    time.sleep(5)
                    uf = update_influx(temperature=temperature,pressure=pressure, humidity=humidity).dynamic_json_update_influx()
		    print("Iteration posted to Influx")
    except KeyboardInterrupt:
        pass
