from control import db2mag
from scipy.signal import iirfilter, lfilter

from plot_helpers import *
from signal_helpers import *

# relevant parameters
critical_frequencies = [5, 10000]
signal_level_db = 0
noise_level_db = -100


# signal parameters
signal_type = "square"  # one of: square, sine, sawtooth, noise
signal_frequency =100

# filter parameters
filter_order = 2

sampling_frequency = 50000

# noise
noise = create_signal("noise", signal_frequency, sampling_frequency)
signal = create_signal(signal_type, signal_frequency, sampling_frequency)

signal_multiplier = db2mag(signal_level_db)
noise_multiplier = db2mag(noise_level_db)
signal = signal_multiplier*signal+noise_multiplier*noise

# filter signal
filter_type = "bandpass"
normalized_filter_frequency = [x / sampling_frequency for x in critical_frequencies]
b, a = iirfilter(filter_order, normalized_filter_frequency, btype=filter_type)
signal = lfilter(b, a, signal)

plt = plot_time_and_frequency_domain(signal, sampling_frequency)
plt.show()
