from cmath import exp, pi

import matplotlib.pyplot as plt
import numpy as np


def FFT(frequencies) -> np.ndarray:
    N = len(frequencies)
    if N <= 1:
        return frequencies

    even = FFT(frequencies[0::2])
    odd = FFT(frequencies[1::2])
    partial = np.zeros(N).astype(np.complex64)

    # Compute up to half the frequencies
    for u in range(N // 2):
        partial[u] = even[u] + exp(-2j * pi * u / N) * odd[u]
        partial[u + N // 2] = even[u] - exp(-2j * pi * u / N) * odd[u]

    return partial


def compute_and_plot_fft(signals, sampling_rate):
    N = len(signals)
    fft_result = FFT(signals)
    freqs = np.fft.fftfreq(N, d=1 / sampling_rate)

    print("\nFFT Result:")
    for idx, entry in enumerate(fft_result):
        print(f"{idx + 1}: {entry}")

    magnitude = np.abs(fft_result)

    # Plot frequency spectrum
    plt.figure()
    plt.stem(
        freqs[: N // 2], magnitude[: N // 2], basefmt=" ", label="Magnitude Spectrum"
    )
    plt.title("Magnitude Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    return fft_result, freqs


def plot_sampled_wave(time, signals):
    plt.figure()
    plt.plot(time, signals, "o-", color="blue", label="Sampled Wave")
    plt.legend()
    plt.title("Plot of Sampled Wave")
    plt.xlabel("Time (t)")
    plt.ylabel("Sampled Signals")
    plt.grid(True)
    plt.show()


def print_header():
    header = "FAST FOURIER TRANSFORM"

    print("-" * 60)
    print(header)
    print("-" * 60)


def evaluate():
    sampling_rate = 20  # Hz
    sampled_time = [
        0.0,
        0.05,
        0.1,
        0.15,
        0.2,
        0.25,
        0.3,
        0.35,
        0.4,
        0.45,
        0.5,
        0.55,
        0.6,
        0.65,
        0.7,
        0.75,
        0.8,
        0.85,
        0.9,
        0.95,
    ]
    sampled_signals = [
        0.00000000e00,
        5.57590997e00,
        2.04087031e00,
        -8.37717508e00,
        -5.02028540e-01,
        1.00000000e01,
        -5.20431056e00,
        -7.68722952e-01,
        -5.56758182e00,
        1.02781920e01,
        1.71450552e-15,
        -1.02781920e01,
        5.56758182e00,
        7.68722952e-01,
        5.20431056e00,
        -1.00000000e01,
        5.02028540e-01,
        8.37717508e00,
        -2.04087031e00,
        -5.57590997e00,
    ]

    print_header()

    print("\nSampling rate: ", sampling_rate)
    print("Sampled time:", sampled_time)
    print("Sampled signals:", sampled_signals)

    # Plot graph of sampled wave:
    # Amplitude against Time
    plot_sampled_wave(sampled_time, sampled_signals)

    # Plot graph of FFT to represent number of physical systems
    # Magnitude against Frequency (Hz)
    compute_and_plot_fft(sampled_signals, sampling_rate)


if __name__ == "__main__":
    evaluate()
