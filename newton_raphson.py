import math
import inspect

def newton_raphson(fx, fx_prime, x0, epsilon, max_iter=100, iteration=0):
    """
        Newton Raphson's method is a root finding algorithm
        that allows successive approximation of the roots of
        a real-valued function

        parameters:
        - fx: the initial function
        - fx_prime: the derivative of the function, fx
        - x0: initial guess
        - epsilon: tolerance threshold
        
        formula:
        - x1 = x0 - fx/fx_prime

        this is a recursive implementation that halts when x1-x0 < epsilon
    """
    if iteration >= max_iter:
        raise Exception("Newton Raphson did not converge")

    f, fp = fx(x0), fx_prime(x0)
    if fp == 0:
        raise Exception("Cannot divide by zero")
    
    if abs(fp) < epsilon:
        raise Exception("Derivative too small")
    
    x1 = x0 - f/fp
    if abs(x1 - x0) < epsilon:
        return x1

    return newton_raphson(fx, fx_prime, x1, epsilon, max_iter, iteration + 1)

def source(fx):
    """
        Helper function to get lambda source text
    """
    text = inspect.getsource(fx)
    text = text.strip()
    text = text.split("lambda x: ")[1]
    return text

if __name__ == "__main__":
    test_cases = [
        {
            "fx": lambda x: 1 - (2 * x * math.pow(math.e, -x/2)),
            "fx_prime": lambda x: math.pow(math.e, -x/2) * (x - 2),
            "x0": 0
        },

        {
            "fx": lambda x: 5 - math.pow(x, -1),
            "fx_prime": lambda x: math.pow(x, -2),
            "x0": 1/4
        },

        {
            "fx": lambda x: math.pow(x, 3) - (2 * x) - 5,
            "fx_prime": lambda x: 3 * math.pow(x, 2) - 2,
            "x0": 2
        }
    ]
    
    EPSILON = 1e-6
    
    print("SOLVING EQUATIONS USING NEWTON-RAPHSON METHOD\n")
    for idx, test in enumerate(test_cases):
        fx = test["fx"]
        fx_prime = test["fx_prime"]
        x0 = test["x0"]  

        print(f"{chr(65 + idx)}")
        print("-" * 35)
        print(f"- f(x): {source(fx)}")
        print(f"- f'(x): {source(fx_prime)}")
        print(f"- x0: {x0}")

        try:
            root = newton_raphson(fx, fx_prime, x0, EPSILON)
            print(f"- found root as: {root}\n")
        except Exception as e:
            print(f"- error: {e}")
