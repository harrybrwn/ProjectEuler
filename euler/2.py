fibs = {}


def fib(n: int) -> int:
    if n <= 1:
        return 1
    if n in fibs:
        return fibs[n]
    left = fib(n-2)
    right = fib(n-1)
    res = left + right
    fibs[n] = res
    return res


def solution() -> int:
    s = 0
    x = 1
    while True:
        v = fib(x)
        if v > 4e6:
            break
        if v % 2 == 0:
            s += v
        x += 1
    return s


def test_solution():
    assert True
    print(solution())
    # print("="*60)
    # for i in range(1, 50):
    #     x = fib(i)
    #     print(str(x) + ("*" if x % 2 == 0 else ""), end=" ")
    # print()
