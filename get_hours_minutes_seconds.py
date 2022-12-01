#NOTE: this version includes days

def get_hours_minutes_seconds(seconds):
    time = ''
    
    if(seconds == 0):
        return '0s'
    
    if seconds // 86400 != 0: #days
        time += str(seconds // 86400) + 'd'
        if seconds % 86400 != 0:
            time += ' '
        seconds %= 86400
    
    if seconds // 3600 != 0: #hours
        time += str(seconds // 3600) + 'h'
        seconds %= 3600
        if seconds % 3600 != 0:
            time += ' '

    if seconds // 60 != 0: #minutes
        time += str(seconds // 60) + 'm'
        seconds %= 60
        if seconds % 60 != 0:
            time += ' '

    if seconds != 0: #seconds
        time += str(seconds) + 's'

    return time

assert get_hours_minutes_seconds(30) == '30s'
assert get_hours_minutes_seconds(60) == '1m'
assert get_hours_minutes_seconds(90) == '1m 30s'
assert get_hours_minutes_seconds(3600) == '1h'
assert get_hours_minutes_seconds(3601) == '1h 1s'
assert get_hours_minutes_seconds(3661) == '1h 1m 1s'
assert get_hours_minutes_seconds(90042) == '1d 1h 42s'
assert get_hours_minutes_seconds(0) == '0s'