import bisect

def sorted_sums(a: list[int]) -> int:
    MOD = 10**9 +7
    sum = 0
    ongoing = []
    for i in range(len(a)):
        ongoing = sorted(a[:i+1])
        for j, num in enumerate(ongoing):

            sum += num*(j+1)
    return sum%MOD


if __name__ == "__main__":
    tests = [
        ([9, 5, 8], 80),
        ([], 0),
        ([5], 5),
        ([1, 2, 3], 20),
        ([3, 2, 1], 25),
        ([2, 2], 8),
        ([4, 1, 3, 2], 62),
        ([10**9, 10**9], 999999979),   # checks the mod
    ]

    for i, (a, expected) in enumerate(tests, 1):
        result = sorted_sums(a)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        if status == "FAIL":
            print(f"  input:    {a}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")