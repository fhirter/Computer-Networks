import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

sampling_frequency = 1000
filter_frequency = 10
period = 5
duty_cycle = 0.1

frequency = 1 / period

# Data for plotting
t = np.linspace(0.0, period, sampling_frequency)

sine = np.sin(2 * np.pi * frequency * t) * 325
sawtooth = signal.sawtooth(2 * np.pi * frequency * t * 2) * 0.5 + 0.5

pwm = sawtooth > duty_cycle

pwm_inverted = np.array(pwm)

#change signal here
input_signal = pwm*sine

## fourier transform
f_orig = np.fft.fft(input_signal)

## sample frequencies
freq = np.fft.fftfreq(len(input_signal), d=t[1]-t[0])

figure1, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(t, input_signal)
ax1.set(xlabel='time (s)', title='Signal')
ax1.grid()

ax2.bar(freq, abs(f_orig) ** 2, 0.3)
ax2.set(xlabel='frequency (Hz)', title='Frequenzspektrum')
ax2.set_xlim(0, frequency * 10)
ax2.grid()
ax2.set_xticks(np.arange(frequency, frequency * 10, step=frequency))

plt.show()
