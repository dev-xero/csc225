import math

from utils import print_header


def center_difference(x, fx, delta):
    """
    Center difference is similar to both forward and backward difference
    methods. We get the value of fx at x + step size and subtract the
    value of fx at x - step size and divide the result by 2 * stepsize

    Formula:
    - f'(x) ~ fx(x+h) - fx(x-h) / (2*h)
    - where h: is the step size, delta
    """
    if delta <= 0:
        raise ValueError("Delta must be positive")
    return (fx(x + delta) - fx(x - delta)) / (2 * delta)


def evaluate():
    test_cases = [
        {"fx": lambda x: math.sin(x), "x": 0, "h": 0.003},
        {"fx": lambda x: math.cos(x), "x": 90, "h": 0.001},
        {"fx": lambda x: math.pow(math.e, x), "x": 2, "h": 0.001},
        {"fx": lambda x: 2 * x, "x": 2, "h": 0.001},
    ]

    print("CENTER DIFFERENCE METHOD\n")
    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        x = test["x"]
        h = test["h"]
        print_header(idx, fx=fx, x=x, h=h)
        derivative = center_difference(x, fx, h)
        print("- found derivative:", derivative)


if __name__ == "__main__":
    evaluate()
