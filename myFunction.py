minutes = input('Choose a number: ')


def minutes_to_hours(minutes):
    hours = int(minutes) / 60
    return hours


seconds = minutes * 60


def seconds_to_hours(seconds):
    hours = seconds / 3600
    return hours


def minutes_to_hour(seconds, minutes=70):
    hours = minutes / 60 + seconds / 3600
    return hours


print(minutes_to_hours(minutes))
print(minutes_to_hour(300))
print(seconds_to_hours(7200))
