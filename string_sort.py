import string

def sort_string(input_string_list):
    alphabet_list_lc = list(string.ascii_lowercase)
    alphabet_list_uc = list(string.ascii_uppercase)
    alphabets = zip(alphabet_list_lc, alphabet_list_uc)
    alphabet_list = [' ']
    sorted_list = []
    for i in alphabets:
        alphabet_list.extend(i)
    for input_name in input_string_list:
        if input_name not in sorted_list:
            for i, name in enumerate(sorted_list):
                inserted = False
                long_name_length = max([len(input_name), len(name)])
                short_name_length = min([len(input_name), len(name)])
                the_shortest = None
                for j in range(short_name_length):
                    if alphabet_list.index(input_name[j]) < alphabet_list.index(name[j]):
                        sorted_list.insert(i, input_name)
                        inserted = True
                        break
                    elif alphabet_list.index(input_name[j]) == alphabet_list.index(name[j]):
                        continue
                    elif alphabet_list.index(input_name[j]) > alphabet_list.index(name[j]):
                        if i < len(sorted_list)-1:
                            break
                        else:
                            sorted_list.append(input_name)
                            inserted = True
                            break
                if inserted:
                    break
                else:
                    continue
            else:
                sorted_list.append(input_name)
        else:
            sorted_list.insert(sorted_list.index(input_name), input_name)
    return sorted_list

alist = ['Anand Nadella', 'Anand Mahadevan', 'Balaji Raman', 'Baalaji', 'Baalaji Raman', 'Jagdeep Singh', 'Aakash Tamilselvan']
slist_no_inbuilt_sort = sort_string(alist)
slist_inbuilt_sort = sorted(alist)

print(slist_no_inbuilt_sort)
print(slist_inbuilt_sort)
