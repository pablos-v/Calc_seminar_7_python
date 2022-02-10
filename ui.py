def inp():
    return input("Введите выражение для калькуляции:")


def check(inp):
    if 'j' in inp:
        return 1
    return 0


def output(res):
    print(res)       