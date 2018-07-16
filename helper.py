import datetime

def pretty_time_format(time):
    hour = time.hour
    min = time.min

    s = str(24 - hour) if (hour > 12) else str(hour)
    s += str(min)

    other = time.strftime('%I:%M:%S on %b %d, %Y').lstrip("0").replace(" 0", " ")
    return other

def pretty_time_format_quick(time):
    hour = time.hour
    min = time.min

    s = str(24 - hour) if (hour > 12) else str(hour)
    s += str(min)

    other = time.strftime('%b %d, %Y').lstrip("0").replace(" 0", " ")
    return other

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False