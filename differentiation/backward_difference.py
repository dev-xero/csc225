import math

from utils import print_header


def backward_difference(x, fx, delta):
    """
    Backward difference is similar to the forward variation, the only difference being in the formula

    Formula:
    - f'(x) ~ [f(x) - f(x-h)] / h
    - where h is the step size, delta

    Returns:
    - approximation of f'(x)
    """
    if delta <= 0:
        raise ValueError("Delta must be positive")
    return (fx(x) - fx(x - delta)) / delta


def evaluate():
    test_cases = [
        {"fx": lambda x: math.sin(x), "x": 0, "h": 0.003},
        {"fx": lambda x: 2 * x, "x": 2, "h": 0.003},
    ]

    print("BACKBWARD DIFFERENCE METHOD\n")
    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        x = test["x"]
        h = test["h"]
        print_header(idx, fx=fx, x=x, h=h)
        derivative = backward_difference(x, fx, h)
        print("- found derivative:", derivative)


if __name__ == "__main__":
    evaluate()
