import pwm_dac
import signal_generator as sg
import time

amplitude = 3
frequency = 100
sampling_frequency = 100

try:
    dac1 = pwm_dac.PWM_DAC(12, frequency, amplitude)
    start = time.time()

    while True:
        current = start - time.time()
        voltage = amplitude * sg.get_sin_wave_amplitude(frequency, current)
        dac1.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac1.deinit()
