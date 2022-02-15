import numpy as np
from scipy import signal as scp_signal


def create_signal(type, signal_frequency, sampling_frequency):
    t = np.linspace(0.0, 2.0, sampling_frequency)
    time_array = 2 * np.pi * t * signal_frequency

    signal = 0
    if type == "square":
        signal = scp_signal.square(time_array)
    if type == "sine":
        signal = np.sin(time_array)
    if type == "sawtooth":
        signal = scp_signal.sawtooth(time_array)
    if type == "noise":
        signal = np.random.rand(sampling_frequency)

    return signal
