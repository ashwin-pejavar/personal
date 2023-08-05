def combinations(input_arr: list[str], choose: int) -> list[list[str]]:
    if choose == 0 or choose > len(input_arr):
        return []
    if choose == len(input_arr):
        return [input_arr]

    result = []
    if choose == 1:
        for c in input_arr:
            result.append([c])
        return result

    for i in range(len(input_arr)):
        combs = combinations(input_arr[i+1:], choose - 1)
        for c in combs:
            c.insert(0, input_arr[i])
        result.extend(combs)

    return result


print(len(combinations(["a", "b", "c", "d", "e"], 3)))
print(combinations(["a", "b", "c", "d", "e"], 3))
