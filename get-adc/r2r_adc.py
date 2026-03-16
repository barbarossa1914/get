import RPi.GPIO as GPIO
import time


class R2R_ADC:

    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.cleanup(self.bits_gpio)

    def number_to_dac(self, number):
        bits =  [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

    def get_sc_voltage(self, num):
        return num  / 255 * self.dynamic_range 

    def sequential_counting_adc(self):
        c = 0
        while c <= 255:
            self.number_to_dac(c)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                return self.get_sc_voltage(c)
                break
            c += 1
        return self.get_sc_voltage(255)
    
    def bin_search(self):
        volt = 0
        for i in range(8):
            volt += 2 ** (7-i)
            self.number_to_dac(volt)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                volt -= 2 ** (7-i)
                
        return self.get_sc_voltage(volt)

if __name__ == '__main__':
    r2r_adc = R2R_ADC(3.3)
    try:
        while True:
            #print(r2r_adc.sequential_counting_adc())
            print(r2r_adc.bin_search())
            time.sleep(0.2)
    finally:
        r2r_adc.deinit()
    

        


