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

    ax2.stem(frequencies, mag2db(abs(yf)), 'b', markerfmt=" ", basefmt="-b")

    ax2.set(
        xlabel='Frequency [Hz]',
        ylabel='Power dB'
    )

    ax2.set_xlim(0, base_frequency * 50)
    ax2.set_ylim(0, 50)

    ax1.grid()
    ax2.grid()
    # ax2.set_xticks(arange(signal_frequency, signal_frequency * 10, step=signal_frequency))

    # figure2, (ax2, ax4) = plt.subplots(2, 1)
    # ax2.plot(t, filtered_square)
    # ax2.set(xlabel='time (s)', title='Lowpass filtered square signal')
    # ax2.grid()
    #
    # ax4.bar(freq, abs(f_filtered)**2, 0.1)
    # ax4.set(xlabel='frequency (Hz)', title='Lowpass Square signal')
    # ax4.set_xlim(0, signal_frequency*10)

    plt.show()
