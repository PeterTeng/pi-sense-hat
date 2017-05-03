from sense_hat import SenseHat
sense = SenseHat()

def show_slow_text(text):
    sense.show_message(text, scroll_speed=0.05, text_colour=[170, 170, 170])

while True:
    temperature = sense.get_temperature()
    pressure    = sense.get_pressure()
    humidity    = sense.get_humidity()

    temperature = round(temperature, 1)
    pressure    = round(pressure, 1)
    humidity    = round(humidity, 1)

    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (temperature, pressure, humidity)

    show_slow_text(msg)
