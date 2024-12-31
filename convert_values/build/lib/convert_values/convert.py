# convert_values/convert.py

import ast

def convert_value(value):
    # Try to safely evaluate the string to its actual type
    try:
        value = ast.literal_eval(value)
    except (ValueError, SyntaxError):
        pass  # If it can't be converted safely, keep the value as it is

    # Handle common cases
    if isinstance(value, bool):
        return value
    elif isinstance(value, int):
        return value
    elif isinstance(value, float):
        return value
    elif isinstance(value, tuple):
        return value  # Return as tuple if it's already a tuple
    elif isinstance(value, list):
        return value  # Return as list if it's already a list
    elif isinstance(value, dict):
        return value  # Return as dict if it's already a dict
    else:
        return str(value)  # Default to string if no match
