from calls import CALLS
from call_log import generate_call_log
from name_log_old import generate_name_log2
from scratch import generate_name_log3
from name_log import generate_name_log
from report import generate_report


def main():
    call_log = generate_call_log(CALLS)
    name_log = generate_name_log(call_log, CALLS)
    # name_log2 = generate_name_log2(call_log, CALLS)
    # name_log3 = generate_name_log3(call_log, CALLS)
    generate_report(name_log)


if __name__ == '__main__':
    main()