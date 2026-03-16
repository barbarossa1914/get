import pwm_dac
import signal_generator as sg
import time

amplitude = 3
frequency = 100
sampling_frequency = 1000

try:
    dac1 = pwm_dac.PWM_DAC(12, frequency, amplitude)

    while True:
        voltage = amplitude* sg.get_sin_wave_amplitude(frequency, time.time())
        dac1.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac1.deinit()
