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

    temperature_text = "%s 'C"　% (temperature)
    sense.show_slow_text(temperature_text)

    pressure_text = "%s hPa"　% (pressure)
    sense.show_slow_text(pressure_text)

    humidity_text = "%s %"　% (humidity)
    sense.show_slow_text(humidity_text)
