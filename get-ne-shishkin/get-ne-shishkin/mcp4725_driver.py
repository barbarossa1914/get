import smbus

class MCP4725():

    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print('На вход ЦАП можно подавать только целые числа')

        if not (0 <= number <= 4095):
            print('Число выходит за разрядность ЦАП')

        first_byte = self.wm | self.pds |number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f'Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02x}, 0x{first_byte:02x}, 0x{second_byte:02x}]\n')
    
    def set_voltage(self, voltage):
        if not 0 <= voltage <= self.dynamic_range:
            print('Напряжение выходит за диапазон')
            return 0
        number = int(voltage / 5 * 4095)
        self.set_number(number)
        return 0
    
if __name__ == '__main__':
    dac = MCP4725(5)
    try:
        while True:
            try:
                voltage = float(input('Введите напряжение в Вольтах: '))
                dac.set_voltage(voltage)
        
            except ValueError:
                print('Вы ввели не число')
        
    finally:
        dac.deinit()


