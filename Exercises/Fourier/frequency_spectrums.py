from scipy.signal import iirfilter, lfilter

from plot_helpers import *
from signal_helpers import *

signal_type = "sine"

sampling_frequency = 1000
signal_frequency = 1

# filter parameters
filter_frequency = 100
filter_order = 5

signal = create_signal(signal_type, signal_frequency, sampling_frequency)

# filter signal
filter_type = "lowpass"
normalized_filter_frequency = filter_frequency / sampling_frequency
b, a = iirfilter(filter_order, normalized_filter_frequency, btype=filter_type)
signal = lfilter(b, a, signal)

plot_time_and_frequency_domain(signal, sampling_frequency)
