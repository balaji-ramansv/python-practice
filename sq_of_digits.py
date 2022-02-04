def square_digits(num):
    """ Square every digit of the passed integer. """
    strnum = str(num)
    final_num = ""
    for ch in strnum:
        ch = int(ch)
        sq = ch ** 2
        final_num += str(sq)
    return final_num

print(square_digits(9119))
