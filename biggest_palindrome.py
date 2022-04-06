from itertools import count
from queue import Empty


def form_biggest_palindrome(s: str):
    count_of_chars = {}
    for c in s:
        if c not in count_of_chars:
            count_of_chars[c] = s.count(c)
    max_odd = {}
    print(count_of_chars)
    palindrome_count = {}
    for i, j in count_of_chars.items():
        if j % 2 and j > 1:
            palindrome_count[i] = j - 1
            if len(max_odd) != 0:
                k = list(max_odd.keys())[0]
                if j > max_odd[k]:
                    max_odd = {i: j}
            else:
                max_odd = {i: j}
        else:
            palindrome_count[i] = j
    max_odd_char, max_odd_char_count = max_odd.popitem()
    pstr = max_odd_char * max_odd_char_count
    print(palindrome_count)
    for pc in palindrome_count:
        if pc == max_odd_char:
            continue
        occurrence = palindrome_count[pc]
        one_side_occ = occurrence // 2
        pstr = f"{pc * one_side_occ}{pstr}{pc * one_side_occ}"
    return pstr

print(form_biggest_palindrome("aaabbbbccd"))
print(form_biggest_palindrome("aaabbbbcccdddbm"))