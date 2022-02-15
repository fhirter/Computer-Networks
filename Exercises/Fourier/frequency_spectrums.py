from scipy.signal import iirfilter, lfilter

from plot_helpers import *
from signal_helpers import *

# signal parameters
signal_type = "square"  # one of: square, sine, sawtooth, noise
signal_frequency =10

# filter parameters
critical_frequencies = [50, 5000]
filter_order = 2

sampling_frequency = 50000
signal = create_signal(signal_type, signal_frequency, sampling_frequency)

# filter signal
filter_type = "bandpass"
normalized_filter_frequency = [x / sampling_frequency for x in critical_frequencies]
b, a = iirfilter(filter_order, normalized_filter_frequency, btype=filter_type)
signal = lfilter(b, a, signal)

plt = plot_time_and_frequency_domain(signal, sampling_frequency)
plt.show()