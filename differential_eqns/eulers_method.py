# ===========================================
# https://en.wikipedia.org/wiki/Euler_method
# ===========================================

import math


def euler(xn, yn, h, f):
    return yn + h * f(xn, yn)


def tabulate_euler(f, x0=0, y0=1, n=20, h=0.1):
    print("-" * 56)
    print(f"{'n':<3} | {'xn':<8} | {'yn':<8} | {'dy/dx':<8} | {'h':<8} | {'yn+1':<8}")
    print("-" * 56)

    x, y = x0, y0

    for i in range(n):
        f_val = f(x, y)
        y_next = euler(x, y, h, f)

        print(
            f"{i:<3} | {x:<8.4f} | {y:<8.4f} | {f_val:<8.4f} | {h:<8.4f} | {y_next:<8.4f}"
        )

        x += h
        y = y_next


def evaluate():
    tests = [
        {"f": lambda x, y: y, "desc": "dy/dx = y", "x0": 0, "y0": 1},
        {"f": lambda x, y: x, "desc": "dy/dx = x", "x0": 0, "y0": 0},
        {"f": lambda x, y: math.sin(x), "desc": "dy/dx = sin(x)", "x0": 0, "y0": 1},
    ]

    print("EULER'S METHOD APPROXIMATION OF SOLUTIONS TO ODEs\n")

    for test in tests:
        print(f"Problem: {test['desc']}")
        print(f"Initial condition: y({test['x0']}) = {test['y0']}")
        tabulate_euler(test["f"], test["x0"], test["y0"])
        print("\n")


if __name__ == "__main__":
    evaluate()
