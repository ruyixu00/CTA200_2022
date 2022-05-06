# part 1
x = float(input("Insert a value of x: "))


def f(x):
    ans = x ** 3 + x ** 2 + 1
    return ans


def df(x):
    ans = 3 * x ** 2 + 2 ** x
    return ans


print(f(x))
print(df(x))
