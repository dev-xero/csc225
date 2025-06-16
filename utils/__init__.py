import inspect
import re


def print_header(idx, **vals):
    print("-" * 55)
    print(f"Problem {chr(65 + idx)}")
    print("-" * 55)

    for key, val in vals.items():
        if callable(val):
            print(f"- {key}: {source(val)}")
        else:
            print(f"- {key}: {val}")


# can be messy
def source(fx):
    text = inspect.getsource(fx).strip()
    match = re.search(r"lambda\s+[^:]+:\s+.*?(?=[,\}])", text)
    if match:
        return match.group()

    return "NONE"


__all__ = ["print_header", "source"]
