import math

import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq
from control import mag2db
import numpy as np


def plot_time_and_frequency_domain(input_signal, sampling_frequency):
    figure1, (ax1, ax2) = plt.subplots(2, 1)
    time_axis = np.linspace(0, 2, num=len(input_signal))

    ax1.plot(time_axis, input_signal, "r")
    ax1.set(
        xlabel='time [s]',
        ylabel='Amplitude',
        title='Time and Frequency Domain'
    )

    yf = abs(fft(input_signal))
    frequencies = fftfreq(len(input_signal), 1 / sampling_frequency) / 2

    base_frequency = np.argmax(np.asarray(yf[0:math.floor(sampling_frequency / 2)])) / 2

    ax1.grid()
    ax1.set_xlim(0, 0.02)

    ax2.grid()
    levels = mag2db(yf)
    levels = levels - max(levels)
    ax2.plot(frequencies, levels, "b")

    ax2.set(
        xlabel='Frequency [Hz]',
        ylabel='Power dBfs'
    )

    frequency_range = 20
    ax2.set_xlim(0, base_frequency * frequency_range)

    ax2.set_ylim(min(levels), max(levels) + 10)
    ax2.set_xticks(np.arange(base_frequency, base_frequency * frequency_range, step=2 * base_frequency))

    figure1.tight_layout()

    return plt
