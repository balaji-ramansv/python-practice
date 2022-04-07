def solutions(digits, num):
    digit_dict = {}
    for i in range(len(digits)):
        digit_dict[digits[i]] = i
    jumps = 0
    prev = None
    for m, n in enumerate(num):
        if m == 0:
            prev = digit_dict[n]
            jumps += prev
        else:
            jumps += abs(digit_dict[n] - prev)
            prev = digit_dict[n]
    return jumps

print(solutions("8459761203", "5439"))
