def rank_the_num(num):
    for_most = {'1': 'st', '2': 'nd', '3': 'rd', '4': 'th', '5': 'th', '6': 'th', '7': 'th', '8': 'th', '9': 'th', '0': 'th'}
    num_str = str(num)
    if (len(num_str) >= 2 and num_str[-2] != '1') or\
            (len(num_str) == 1):
        return f"{num_str}{for_most[num_str[-1]]}"
    else:
        return f"{num_str}th"

print(rank_the_num(1))
print(rank_the_num(2))
print(rank_the_num(3))
print(rank_the_num(4))
print(rank_the_num(10))
print(rank_the_num(11))
print(rank_the_num(19))
print(rank_the_num(23))
print(rank_the_num(99))
print(rank_the_num(100))
print(rank_the_num(111))
print(rank_the_num(123))