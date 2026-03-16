import RPi.GPIO as GPIO

class PWM_DAC():

    def __init__(self, gpio_pin, pwm_frquency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frquency
        self.dynamic_range = dynamic_range

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    
    def set_voltage(self, voltage):
        duty = voltage/self.dynamic_range
        return GPIO.PWM(self.gpio_pin, duty)

if __name__ == '__main__':
    dac = PWM_DAC(12, 500, 3.290, True)
    try:
        while True:
            try:
                voltage = float(input('Введите напряжение в вольтах'))
                dac.set_voltage

            except ValueError:
                print('Вы ввели не число\n')
    finally:
        dac.deinit()
        dac.set_voltage