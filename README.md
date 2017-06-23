Shift Register 74HC595
=======

Dynamic class to manage Shift Register 74HC595 in Raspberry Pi using Python

## Requirements

    * Raspberry Pi
    * Python 2.6+ and Python development tools
    * RPi.GPIO (latest version recommended)

## Installation

Install RPi.GPIO library and Python development tools:

``` bash
sudo apt-get update && sudo apt-get -y install python-rpi.gpio python-dev
```

Get this library:

``` bash
git clone git@github.com:marsminds/shiftr_74HC595.git
```

## Example
![Scheme](http://marsminds.com/wp-content/uploads/2015/09/74hc595_leds_bb.jpg)

``` python
import RPi.GPIO as GPIO
from shiftr_74HC595.shiftr_74HC595 import ShiftRegister
from time import sleep

GPIO.setmode(GPIO.BOARD)

data_pin = 7 #pin 14 on the 75HC595
latch_pin = 11 #pin 12 on the 75HC595
clock_pin = 12 #pin 11 on the 75HC595

shift_register = ShiftRegister(data_pin, latch_pin, clock_pin)

try:
    while 1:
        # Set all outputs
        shift_register.setOutputs([GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH])

        # Display
        shift_register.latch()

        sleep(1)

        # Set some output individually
        shift_register.setOutput(0, GPIO.LOW)
        shift_register.setOutput(5, GPIO.HIGH)

        shift_register.latch()

        sleep(1)
except KeyboardInterrupt:
    print "Ctrl-C - quit"

GPIO.cleanup()
```

## API

### Constructor

Instanciate and configure pin of a shift register.

``` python
ShiftRegister(data_pin, latch_pin, clock_pin)
```

    data_pin => pin 14 on the 74HC595
    latch_pin => pin 12 on the 74HC595
    clock_pin => pin 11 on the 74HC595

Example:

``` python
# Instanciate a new shiftregister wired on pins 14, 15, 18 of the Raspberry
shift_register = ShiftRegister(14, 15, 18)
```

### Method setOutput

Update an individual output of the shift register.

``` python
shift_register.setOutput(output_number, value)
```

    output_number => Value from 0 to 7 pointing to the output pin on the 74HC595
    0 => Q0 pin 15 on the 74HC595
    1 => Q1 pin 1 on the 74HC595
    2 => Q2 pin 2 on the 74HC595
    3 => Q3 pin 3 on the 74HC595
    4 => Q4 pin 4 on the 74HC595
    5 => Q5 pin 5 on the 74HC595
    6 => Q6 pin 6 on the 74HC595
    7 => Q7 pin 7 on the 74HC595

    value => a state to pass to the pin, could be HIGH or LOW

Example:

``` python
# Set Q3 to high in register
shift_register.setOutput(3, GPIO.HIGH)

shift_register.latch()
```

### Method setOutputs

Update all outputs of the shift register.

``` python
shift_register.setOutputs(outputs)
```

    outputs => an array of height GPIO.LOW or GPIO.HIGH

Example:

``` python
# Draw a zebra
shift_register.setOutputs([GPIO.LOW, GPIO.HIGH,  GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.HIGH])

shift_register.latch()
```

### Method latch

Clock the shift register so the updated values are sent to shift register outputs.

``` python
shift_register.latch()
```

Example:

``` python
# Perform some updates...
shift_register.setOutput(3, GPIO.HIGH)

# Display result
shift_register.latch()
```
