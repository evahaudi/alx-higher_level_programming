#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        divde = a / b
    except (TypeError, ZeroDivisionError):
        divde = None
    finally:
        print("Inside result: {}".format(divde))
    return (divde)
