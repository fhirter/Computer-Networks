import numpy as np
from scipy.signal import iirfilter, lfilter, square


from plot_helpers import *

sampling_frequency = int(50000)
carrier_frequency = int(500)
signal_frequency = int(10)

ac = 0.3 # modulation index

# filter parameters
critical_frequencies = [400, 600]
filter_order = 2

frequency_domain_range = 5    # adjust shown frequency range

t = np.linspace(0.0, 2.0, sampling_frequency)
time_array = 2 * np.pi * t

carrier = np.sin(time_array * carrier_frequency)
data_signal = square(time_array * signal_frequency)
signal = (1 + data_signal/ac) * carrier

# filter signal
filter_type = "bandpass"
normalized_filter_frequency = [x / sampling_frequency for x in critical_frequencies]
b, a = iirfilter(filter_order, normalized_filter_frequency, btype=filter_type)
signal = lfilter(b, a, signal)

plt = plot_time_and_frequency_domain(signal, sampling_frequency)

figure = plt.figure(1)
axes = figure.get_axes()

axes[1].set_xticks(np.arange(0, 1000, step=carrier_frequency/(frequency_domain_range*4)))
axes[1].set_xlim(carrier_frequency-carrier_frequency/frequency_domain_range, carrier_frequency+carrier_frequency/frequency_domain_range)

plt.show()
