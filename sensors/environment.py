from sense_hat import SenseHat
sense = SenseHat()

def show_slow_text(text):
    sense.show_message(text, scroll_speed=0.05, text_colour=[120, 120, 120])

while True:
    temperature = sense.get_temperature()
    pressure    = sense.get_pressure()
    humidity    = sense.get_humidity()

    temperature = round(temperature, 1)
    pressure    = round(pressure, 1)
    humidity    = round(humidity, 1)

    temperature_text = "%s C" % (temperature)
    humidity_text = "%s %" % (humidity)
    pressure_text = "%s hpa" % (pressure)

    show_slow_text(temperature_text)

    show_slow_text(humidity_text)

    show_slow_text(pressure_text)
