import numpy as np
import time

def get_sin_wave_amplitude(freq, ti):
    return (np.sin(2*np.pi*freq*ti) + 1) / 2

def wait_for_sampling_period(samp_freq):
    time.sleep(1/samp_freq)
    return 

