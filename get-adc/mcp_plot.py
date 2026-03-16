import mcp3021_driver as mc
import adc_plot as ap
import time
import matplotlib.pyplot as plt

mcp = mc.MCP3021(5)
voltage_values = []
time_values = []
periods = []
duration = 3.0

try:
    start = time.time()
    prev = start
    current = start
    while current - start < duration:
        voltage_values.append(mcp.get_voltage())
        time_values.append(current-start)
        ap.fill_periods(periods, prev, current)
        prev = current
        current = time.time()
    ap.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    ap.plot_sampling_period_hist(periods)
        
finally:
    mcp.deinit()