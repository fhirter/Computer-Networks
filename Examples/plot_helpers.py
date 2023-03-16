import math

import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq
from control import mag2db
import numpy as np


def plot_time_and_frequency_domain(input_signal, sampling_frequency):
    figure1, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(input_signal)
    ax1.set(
        xlabel='time [s]',
        ylabel='Amplitude',
        title='Time and Frequency Domain'
    )

    yf = abs(fft(input_signal))
    frequencies = fftfreq(len(input_signal), 1 / sampling_frequency) / 2

    base_frequency = np.argmax(np.asarray(yf[0:math.floor(sampling_frequency / 2)])) / 2

    ax1.grid()

    ax2.grid()
    levels = mag2db(yf)
    ax2.stem(frequencies, levels, 'b', markerfmt=" ", basefmt="-b")

    ax2.set(
        xlabel='Frequency [Hz]',
        ylabel='Power dB'
    )

    ax1.set_xlim(0, sampling_frequency/base_frequency)

    ax2.set_xlim(0, base_frequency * 100)

    ax2.set_ylim(min(levels)-10, max(levels)+10)
    ax2.set_xticks(np.arange(base_frequency, base_frequency * 100, step=10 * base_frequency))

    return plt
