Shift Register 74HC595
=======

Dynamic class to manage Shift Register 74HC595 in Raspberry Pi using Python

#Requirements

    * Raspberry Pi
    * Python 2.6+ and Python development tools
    * RPi.GPIO (latest version recommended)

#Installation

    Install RPi.GPIO library and Python development tools:

        # sudo apt-get update && sudo apt-get -y install python-rpi.gpio python-dev

    Get this library:

        # git clone git@github.com:marsminds/shiftr_74HC595.git


#Example
![Scheme](http://i.picresize.com/images/2014/03/11/xM26G.jpg)

    import RPi.GPIO as GPIO
    from shiftr_74HC595.shiftr_74HC595 import ShifRegister
    from time import sleep

    GPIO.setmode(GPIO.BOARD)

    data_pin = 7 #pin 14 on the 75HC595
    latch_pin = 11 #pin 12 on the 75HC595
    clock_pin = 12 #pin 11 on the 75HC595
    shift_register = ShifRegister(data_pin, latch_pin, clock_pin)

    try:
        while 1:
            shift_register.setOutput(0, GPIO.HIGH)
            shift_register.setOutput(1, GPIO.LOW)
            shift_register.setOutput(2, GPIO.LOW)
            shift_register.setOutput(3, GPIO.LOW)
            shift_register.setOutput(4, GPIO.HIGH)
            shift_register.setOutput(5, GPIO.LOW)
            shift_register.setOutput(6, GPIO.LOW)
            shift_register.setOutput(7, GPIO.HIGH)
            sleep(1)

            shift_register.setOutput(0, GPIO.LOW)
            shift_register.setOutput(1, GPIO.HIGH)
            shift_register.setOutput(2, GPIO.HIGH)
            shift_register.setOutput(3, GPIO.HIGH)
            shift_register.setOutput(4, GPIO.LOW)
            shift_register.setOutput(5, GPIO.HIGH)
            shift_register.setOutput(6, GPIO.HIGH)
            shift_register.setOutput(7, GPIO.LOW)
            sleep(1)
    except KeyboardInterrupt:
        print "Ctrl-C - quit"

    GPIO.cleanup()

## Class ShifRegister(data_pin, latch_pin, clock_pin)
    data_pin => pin 14 on the 74HC595
    latch_pin => pin 12 on the 74HC595
    clock_pin => pin 11 on the 74HC595

## Method setOutput(output_number, value)
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
