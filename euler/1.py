def solution(n: int) -> int:
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)

def test_solution():
    n = solution(1000)
    print(n)
    assert n > 0
    assert n > 23 # result for 10
    assert solution(10) == 23
