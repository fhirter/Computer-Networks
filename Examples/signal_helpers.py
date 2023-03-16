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
        n = len(t)
        x = np.random.randn(n)
        variance = np.sum(x**2) / n
        scale_factor = 1 / np.sqrt(variance)

        signal = x * scale_factor

        # shift the signal to have mean of 0
        mean_value = np.mean(signal)
        signal -= mean_value

        rms = np.sqrt(np.mean(signal ** 2))
        mean = np.mean(signal)

    return signal
