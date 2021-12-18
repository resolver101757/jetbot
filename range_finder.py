import time
import board
import busio
import adafruit_vl6180x

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor instance.
sensor = adafruit_vl6180x.VL6180X(i2c)
# You can add an offset to distance measurements here (e.g. calibration)
# Swapping for the following would add a +10 millimeter offset to measurements:
# sensor = adafruit_vl6180x.VL6180X(i2c, offset=10)

def get_range():
    # Read the range in millimeters and print it.
    range_mm = sensor.range
    print("Range: {0}mm".format(range_mm))
    time.sleep(1.0)
    return range_mm

# def main():
#     while True:
#         get_range()

# if __name__ == "__main__":
#     main()