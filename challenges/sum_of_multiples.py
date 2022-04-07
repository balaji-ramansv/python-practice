def solution1(number):
    multiples = []
    for m in [3,5]:
        counter = 1
        while (m * counter) < number:
            prod = m * counter
            if prod not in multiples:
                multiples.append(prod)
            counter += 1
    return sum(multiples)

def solution2(number):
    overall = set()
    for n in [3, 5]:
        overall.update({ i for i in range(n, number, n) })
    return sum(list(overall))



print(solution1(16))
print(solution2(16))

