def time_format(time):
    hour = time.hour
    min = time.min

    s = str(24 - hour) if (hour > 12) else str(hour)
    s += str(min)

    other = time.strftime('%I:%M on %b %d, %Y').lstrip("0").replace(" 0", " ")
    return other
