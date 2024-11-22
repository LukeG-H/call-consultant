from datetime import timedelta
import time

def convert_time_str_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


def generate_report(name_log):
    total_talking_time = 0
    print("Daily Call Log\nTotal Talking Time by Person (Phone Number) (hh:mm:ss):\n")

    for name, call_durations in name_log.items():
        # create a list of call duration ints (seconds), converted from strs, for each value associated with the key (name):
        call_durations_seconds = [convert_time_str_to_seconds(duration) for duration in call_durations]
        # sum the list of durations for each key (name):
        phone_number_talking_time = sum(call_durations_seconds)
        # add the summed durations to the total:
        total_talking_time += phone_number_talking_time
        print(f'{name}: {timedelta(seconds=phone_number_talking_time)}')

    print(f'\nTotal Daily Talking Time: {timedelta(seconds=total_talking_time)}')
    # time.sleep(10)