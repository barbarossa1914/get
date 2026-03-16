import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title('Зависимость напряжения от времени')
    plt.xlabel('Время')
    plt.ylabel('Напряжение')
    plt.grid()
    plt.show()
    
def plot_sampling_period_hist(sampling_periods):
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.title('Зависимость частоты дискретизации от времени')
    plt.xlabel('Время')
    plt.ylabel('Количество измерений напряжения')
    plt.grid()
    plt.show()

def fill_periods(arr, st, end):
    delta = end - st
    arr.append(delta)
    