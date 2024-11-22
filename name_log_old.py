# from calls import CALLS
# from call_log import generate_call_log

def generate_name_log2(call_log, calls):
    name_log = {}
    name_counter = {}   # count the duplicate names

    for number, durations in call_log.items():
        for call in calls:  # look at each call in the call list
            if number == call.number and call.name not in name_log:  # when call_log number matches call list number, and caller name is not in name_log 
                name_log[call.name] = durations # ADD name as the key with the matching values from call_log
                name_counter[call.name] = 1 # Initialise counter for the name

            elif number == call.number and call.name in name_log:   # when call_log number matches call list number, and caller name is in name log
                if call.length not in name_log[call.name]:  # check if call length is already a value assigned to the name key in name_log
                    name_key = f"{call.name}{name_counter[call.name]} @ {call.number}"  # a new key is created which is the concatenation of the name and it's count (value of the name_counter)
                    name_log[name_key] = durations  # ADD name_key as new key to name_log with it's values
                    name_counter[call.name] += 1    # increment the name_counter by 1 for that name
            else:
                continue
    return(name_log)

# DONE: inner loop is catching people with multiple calls and creating a new key in the log, or overwriting existing values
# FIXME: if the number is different, but the caller has the same name, and call length exists as a value for that name, the call is ignored and and not added to the name_log as a new key
# DONE: multiple duplicates don't work with name_count as it is holding ALL duplicates not duplicate per name

# call_log = generate_call_log(CALLS)
# name_log = generate_name_log2(call_log,CALLS)
# print(name_log)