import RPi.GPIO as GPIO

class ShifRegister:
    register_type = '74HC595'

    """
    data_pin => pin 14 on the 74HC595
    latch_pin => pin 12 on the 74HC595
    clock_pin => pin 11 on the 74HC595
    """
    def __init__(self, data_pin, latch_pin, clock_pin):
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin

        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)

        self.outputs = [0, 0, 0, 0, 0, 0, 0, 0]

    """
    output_number => Value from 0 to 7 pointing to the output pin on the 74HC595
    Values:
    0 => Q0 pin 15 on the 74HC595
    1 => Q1 pin 1 on the 74HC595
    2 => Q2 pin 2 on the 74HC595
    3 => Q3 pin 3 on the 74HC595
    4 => Q4 pin 4 on the 74HC595
    5 => Q5 pin 5 on the 74HC595
    6 => Q6 pin 6 on the 74HC595
    7 => Q7 pin 7 on the 74HC595
    """
    def setOutput(self, output_number, value):
        try:
            self.outputs[output_number] = value
        except IndexError:
            raise ValueError("Invalid output number. Can be only an int from 0 to 7")

        GPIO.output(self.latch_pin, GPIO.LOW)
        for output in range(7, -1, -1):
            GPIO.output(self.clock_pin, GPIO.LOW)

            value = self.outputs[output]

            GPIO.output(self.data_pin, value)
            GPIO.output(self.clock_pin, GPIO.HIGH)

        GPIO.output(self.latch_pin, GPIO.HIGH)
