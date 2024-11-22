from calls import CALLS

def generate_call_log(calls):
    call_log = {}
    name_count = {}

    for call in calls:
        name = call.name
        number = call.number
        duration = call.length

        if number not in call_log:
            call_log[number] = list()
        call_log[number].append(duration)
    return call_log

call_log = generate_call_log(CALLS)
print(f"{call_log}\n")