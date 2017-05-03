from sense_hat import SenseHat

sense = SenseHat()

# 1st Column
sense.set_pixel(0, 2, [0, 0, 255])
sense.set_pixel(0, 3, [0, 0, 255])
sense.set_pixel(0, 4, [0, 0, 255])
sense.set_pixel(0, 5, [0, 0, 255])

# 2nd Column
sense.set_pixel(1, 3, [0, 0, 255])
sense.set_pixel(1, 4, [0, 0, 255])

# 3rd Column
sense.set_pixel(0, 1, [0, 0, 255])
sense.set_pixel(0, 2, [0, 0, 255])
sense.set_pixel(0, 3, [0, 0, 255])
sense.set_pixel(0, 4, [0, 0, 255])
sense.set_pixel(0, 5, [0, 0, 255])
sense.set_pixel(0, 6, [0, 0, 255])

# 4th Column
sense.set_pixel(0, 2, [0, 0, 255])
sense.set_pixel(0, 3, [0, 0, 255])
sense.set_pixel(0, 4, [0, 0, 255])
sense.set_pixel(0, 5, [0, 0, 255])

# TODO(peterteng) - Revert Algorithm

sense.clear()
