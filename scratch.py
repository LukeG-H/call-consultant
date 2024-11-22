from calls import CALLS
from call_log import generate_call_log

def generate_name_log3(call_log, calls):
    name_log = {}
    name_counter = {}

    for call in calls:
        if call.number in call_log:
            name = call.name
            number = call.number
            durations = call_log[number]
            
            if name not in name_log:
                name_counter[name] = 1
                name_log[name] = durations
            
            else: 
                # if call.length not in name_log[name]: 
                    name_number_key = f"{name}{name_counter[name]} @ {number}"
                    name_counter[name] += 1
                    name_log[name_number_key] = durations
    return name_log

# FIXME: if the number is different, but the caller has the same name, and call length exists as a value for that name, the call is ignored and and not added to the name_log as a new key
# call_log = generate_call_log(CALLS)
# name_log = generate_name_log3(call_log, CALLS)
# print(name_log)