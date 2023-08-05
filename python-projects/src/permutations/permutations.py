def remove(input_arr: list, idx: int) -> list:
    result = list(input_arr)
    del result[idx]
    return result


def permutations(input_arr: list[str]) -> list[list[str]]:
    if len(input_arr) == 1:
        return [input_arr]

    result = []
    for i in range(len(input_arr)):
        perms = permutations(remove(input_arr, i))
        for perm in perms:
            perm.insert(0, input_arr[i])
        result.extend(perms)

    return result


print(len(permutations(["a", "b", "c", "d", "e"])))
print(permutations(["a", "b", "c", "d", "e"]))