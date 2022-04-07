def get_set_from_file(filename):
    emails = set()
    with open(filename, "r") as f:
        for email in f.readlines():
            emails.add(email.strip())
    return emails

def print_set(message, set_to_print):
    line = "#" * (len(message) + 6)
    print(f"{line}\n## {message} ##\n{line}")
    for item in set_to_print:
        print(item)
    if len(set_to_print) == 0:
        print("None")
    print("\n\n")

if __name__ == "__main__":
    cal_set = get_set_from_file(r"d:\pyfiles\emails_diff\current_cal.txt")
    space_set = get_set_from_file(r"d:\pyfiles\emails_diff\current_space.txt")

    # Present in space but not in calender yet
    space_minus_cal = space_set.difference(cal_set)
    print_set("Add below engineers to calendar", space_minus_cal)

    # Present in calendar but not in space yet
    cal_minus_space = cal_set.difference(space_set)
    print_set("Add below engineers to space", cal_minus_space)
