from array import array


def fibonacci(terms: int) -> array:
    if terms == 0:
        return [0]
    elif terms == 1:
        return [0, 1]

    result = fibonacci(terms - 1)
    result.append(result[terms - 1] + result[terms - 2])
    return result


print(fibonacci(10))