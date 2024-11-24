# https://www.codewars.com/kata/52742f58faf5485cae000b9a 

def format_duration(seconds):
    time = {
        "year": 31536000,
        "day": 86400,
        "hour": 3600,
        "minute": 60,
        "second": 1
    }
    res = []

    if seconds == 0:
        return "now"

    for key, value in time.items():
        if seconds >= value:
            val = seconds // value
            res.append(f"{val} {key}{'s' if val > 1 else ''}")
            seconds %= value

    if len(res) > 1:
        return ", ".join(res[:-1]) + " and " + res[-1]
    else:
        return res[0]
    