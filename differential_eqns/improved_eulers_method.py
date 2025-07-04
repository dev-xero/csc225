# =============================================
# https://en.wikipedia.org/wiki/Heun%27s_method
# =============================================

import math


def improved_euler(xn, yn, h, f):
    """Improved Euler's Method (Heun's Method)"""
    k1 = f(xn, yn)
    y_pred = yn + h * k1
    k2 = f(xn + h, y_pred)
    # corrector step, take average
    return yn + (0.5 * h) * (k1 + k2)


def tabulate_improved_euler(f, x0=0, y0=1, n=20, h=0.1):
    print("-" * 72)
    print(
        f"{'n':<3} | {'xn':<8} | {'yn':<8} | {'k1':<8} | {'y_pred':<8} | {'k2':<8} | {'yn+1':<8}"
    )
    print("-" * 72)

    x, y = x0, y0
    for i in range(n):
        k1 = f(x, y)
        y_pred = y + h * k1
        k2 = f(x + h, y_pred)
        y_next = improved_euler(x, y, h, f)

        print(
            f"{i:<3} | {x:<8.4f} | {y:<8.4f} | {k1:<8.4f} | {y_pred:<8.4f} | {k2:<8.4f} | {y_next:<8.4f}"
        )

        x += h
        y = y_next


def evaluate():
    tests = [
        {"f": lambda x, y: y, "desc": "dy/dx = y", "x0": 0, "y0": 1},
        {"f": lambda x, y: x, "desc": "dy/dx = x", "x0": 0, "y0": 0},
        {"f": lambda x, y: math.sin(x), "desc": "dy/dx = sin(x)", "x0": 0, "y0": 1},
        {"f": lambda x, y: x + y, "desc": "dy/dx = x + y", "x0": 0, "y0": 1},
    ]

    print(
        "IMPROVED EULER'S METHOD (HEUN'S METHOD) APPROXIMATION OF SOLUTIONS TO ODEs\n"
    )

    for test in tests:
        print(f"Problem: {test['desc']}")
        print(f"Initial condition: y({test['x0']}) = {test['y0']}")
        tabulate_improved_euler(test["f"], test["x0"], test["y0"])
        print("\n")


if __name__ == "__main__":
    evaluate()
