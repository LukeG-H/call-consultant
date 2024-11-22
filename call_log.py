from calls import CALLS

def generate_call_log(calls):
    call_log = {}    
    for call in calls:
        if call.number not in call_log:
            call_log[call.number] = list()
        call_log[call.number].append(call.length)
    return call_log

call_log = generate_call_log(CALLS)
print(f"{call_log}\n")