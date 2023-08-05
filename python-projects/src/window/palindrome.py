def longest_plaindrome(arg: str) -> str:
    result = ""
    # odd
    for i in range(len(arg)):
        begin = end = i
        while begin >= 0 and end < len(arg) and arg[begin] == arg[end]:
            begin -= 1
            end += 1
        if end - begin + 1 > len(result):
            result = arg[begin+1:end]

    # even
    for i in range(len(arg) - 1):
        begin, end = (i, i + 1)
        while begin >= 0 and end < len(arg) and arg[begin] == arg[end]:
            begin -= 1
            end += 1
        if end - begin + 1 > len(result):
            result = arg[begin+1:end]

    return result


print(longest_plaindrome("abcmalyaylamkomriirmokldgjlgdflfdludoguldgflougdf"))
