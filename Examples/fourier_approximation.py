import numpy as np

from plot_helpers import *

# see http://www.thomasborer.ch/mathematik_alt/m_te_fr.pdf for examples
signal_frequencies = [1, 2, 3, 4]
signal_amplitudes = [1, 1/2, 1/3, 1/4]

sampling_frequency = 1000

t = np.linspace(0.0, 2.0, sampling_frequency)
time_array = 2 * np.pi * t

for index, signal_frequency in enumerate(signal_frequencies):
    if index == 0:
        signal = np.sin(time_array * signal_frequency)
    else:
        signal += signal_amplitudes[index]*np.sin(time_array * signal_frequency)

plt = plot_time_and_frequency_domain(signal, sampling_frequency)
plt.show();