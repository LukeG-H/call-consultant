# from calls import CALLS
# from call_log import generate_call_log

def generate_name_log(call_log, calls):
    name_log = {}
    
    for call in calls:
        if call.number in call_log:
            name = call.name
            number = call.number
            durations = call_log[number]
            name_number_key = f"{name} @ {number}"
            name_log[name_number_key] = durations
    return name_log
    

# call_log = generate_call_log(CALLS)
# name_log = generate_name_log(call_log,CALLS)
# print(name_log)