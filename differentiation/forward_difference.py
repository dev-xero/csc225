from utils import print_header


def forward_difference(x, fx, delta):
    """
    The forward difference method allows us to approximate the
    derivative of real functions at a given point

    Formula:
    - f'(x) ~ [f(x+h) - f(x)] / h
    - where h is the step size, delta

    Parameters:
    - x: point at which to approximate derivative
    - fx: function of x
    - delta: step size

    Returns:
    - approximation of f'(x)
    """
    if delta <= 0:
        raise ValueError("Delta must be positive")
    return (fx(x + delta) - fx(x)) / delta


def evaluate():
    test_cases = [
        {"fx": lambda x: x**2, "x": 2, "h": 0.001},
        {"fx": lambda x: 2 * x, "x": 2, "h": 0.001},
    ]
    print("FORWARD DIFFERENCE METHOD\n")
    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        x = test["x"]
        h = test["h"]
        print_header(idx, fx=fx, x=x, h=h)
        derivative = forward_difference(x, fx, h)
        print("- found derivative:", derivative)


if __name__ == "__main__":
    evaluate()
