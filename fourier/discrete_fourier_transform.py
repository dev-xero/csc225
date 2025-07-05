import cmath
import matplotlib.pyplot as plt


def dft(x):
    """
    Idea:
    The Discrete Fourier Transform (DFT) is an algorithm used to compute the Fourier Transform on a discrete data space.

    Formula:
    - Xk = sum(xe^{-2πi * kn / N}) from n = 0 to N-1
    - where:
        - Xk = result of DFT at point k
    """
    N = len(x)
    X = []
    for k in range(N):
        Xk = 0
        for n in range(N):
            alpha = -2j * cmath.pi * k * n / N
            Xk += x[n] * cmath.exp(alpha)
        X.append(Xk)
    return X


def plot_dft(frequencies, magnitudes):
    plt.stem(frequencies, magnitudes, basefmt=" ", label="DFT Magnitude")
    plt.legend()
    plt.title("Discrete Fourier Transforms on Evenly Spaced Intervals")
    plt.xlabel("Frequency Bins (Hz)")
    plt.ylabel("DFT Amplitude |X[freq]|")
    plt.grid(True)
    plt.show()


def evaluate():
    sampling_rate = 20
    sampled_time = [0., 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
                    0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    sampled_signals = [0.00000000e+00, 5.57590997e+00, 2.04087031e+00, -8.37717508e+00, -5.02028540e-01,
                       1.00000000e+01, -5.20431056e+00, -7.68722952e-01, -5.56758182e+00, 1.02781920e+01,
                       1.71450552e-15, -1.02781920e+01, 5.56758182e+00, 7.68722952e-01, 5.20431056e+00,
                       -1.00000000e+01, 5.02028540e-01, 8.37717508e+00, -2.04087031e+00, -5.57590997e+00]

    N = len(sampled_signals)
    freq_bins = dft(sampled_signals)

    frequencies = [k * sampling_rate / N for k in range(N)]
    magnitudes = [abs(Xk) for Xk in freq_bins]

    header = "\nDISCRETE FOURIER TRANSFORM (DFT) ON EVENLY SPACED SAMPLED SIGNALS"
    print(header)
    print("-" * len(header))

    print("Sampling Rate: 20Hz per second")
    print("Sampled Time:", sampled_time)
    print("Sampled Signals:", sampled_signals)
    print("Frequencies:", frequencies)
    print("Magnitudes:", magnitudes)

    plot_dft(frequencies, magnitudes)


if __name__ == "__main__":
    evaluate()
