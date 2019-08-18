# Put helper functions here

def string_safe_int(string):
    try:
        return int(string)
    except ValueError:
        return -1