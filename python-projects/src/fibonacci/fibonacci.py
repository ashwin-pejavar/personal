def fibonacci(terms: int) -> int:
    if terms == 0:
        return 0
    elif terms == 1:
        return 1

    return fibonacci(terms - 1) + fibonacci(terms - 2)


print(fibonacci(9))


