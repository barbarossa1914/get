import RPi.GPIO as GPIO

class PWM_DAC():

    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.pwm = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)


    def deinit(self):
        if self.pwm:
            self.pwm.stop()
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not 0 <= voltage <= self.dynamic_range:
            print('Напряжение выходит за диапазон')
            return 0
        if not self.pwm:
            self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        duty = voltage/self.dynamic_range*100
        self.pwm.ChangeDutyCycle(duty)
        return 
        
"""
if __name__ == '__main__':
    dac = PWM_DAC(12, 1000, 3.0, True)
    try:
        while True:
            try:
                voltage = float(input('Введите напряжение в Вольтах: '))
                dac.set_voltage(voltage)

            
            except ValueError:
                print('Вы ввели не число')
        
    finally:
        dac.deinit()
"""
