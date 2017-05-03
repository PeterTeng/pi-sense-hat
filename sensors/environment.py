from sense_hat import SenseHat
sense = SenseHat()

while True:
    temperature = sense.get_temperature()
    pressure    = sense.get_pressure()
    humidity    = sense.get_humidity()

    temperature = round(temperature, 1)
    pressure    = round(pressure, 1)
    humidity    = round(humidity, 1)

    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (temperature, pressure, humidity)

    sense.show_message(msg, scroll_speed=0.05)
