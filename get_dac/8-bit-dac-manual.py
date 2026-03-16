import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pins = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.1
GPIO.setup(pins, GPIO.OUT)

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print('Устанавливаем 0.0 В')
        return 0
    
    return int(voltage / dynamic_range * 255)



def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while True:
        try:
            voltage = float(input('Введите напряжение в Вольтах: '))
            number = voltage_to_number(voltage)
            GPIO.output(pins, number_to_dac(voltage_to_number(voltage)))

        except ValueError:
            print('Вы ввели не число\n')
        
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()
