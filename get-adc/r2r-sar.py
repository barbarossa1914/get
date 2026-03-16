import r2r_adc as ra
import adc_plot as ap
import time
import matplotlib.pyplot as plt

r2r__adc = ra.R2R_ADC(3.3, 0.0001)
voltage_values = []
time_values = []
periods = []
duration = 3.0

try:
    start = time.time()
    prev = start
    current = start
    while current - start < duration:
        voltage_values.append(r2r__adc.bin_search())
        time_values.append(current-start)
        ap.fill_periods(periods, prev, current)
        prev = current
        current = time.time()
    ap.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    ap.plot_sampling_period_hist(periods)
        
finally:
    r2r__adc.deinit()