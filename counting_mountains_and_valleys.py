from concurrent.futures import process


def counting_valleys(path):
    pathnum = tuple(map(lambda x: 1 if x == 'U' else -1, path))
    processed = []
    valleys = 0
    for i in pathnum:
        processed.append(i)
        if sum(processed) == 0:
            if i == 1:
                valleys += 1
    return valleys


print(counting_valleys("UDDDUDUU"))