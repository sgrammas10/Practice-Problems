import bisect

def largest_area(w: int, h: int, cuts: list[tuple[int, int]]) -> list[int]:
    # your solution here
    area = []
    width = [0,w]
    max_w=0
    height = [0,h]
    max_h=0
    for isv, num in cuts:
        if isv == 1:
            bisect.insort(width, num)
            for i in range(1,len(width)):
                max_w= max(max_w,width[i]-width[i-1])

            
            for i in range(1,len(height)):
                max_h= max(max_h,height[i]-height[i-1])
            area.append(max_w*max_h)
            max_w=0
            max_h=0

        else:
            bisect.insort(height, num)
            for i in range(1,len(height)):
                max_h= max(max_h,height[i]-height[i-1])

            for i in range(1,len(width)):
                max_w= max(max_w,width[i]-width[i-1])
            area.append(max_w*max_h)
            max_w=0
            max_h=0
    return area


if __name__ == "__main__":
    tests = [
        (4, 4, [(1, 1), (0, 2), (1, 3)], [12, 6, 4]),
        (5, 3, [], []),
        (10, 10, [(1, 5)], [50]),
        (10, 10, [(0, 5)], [50]),
        (6, 4, [(1, 2), (1, 4), (0, 1)], [16, 8, 6]),
        (8, 8, [(1, 4), (1, 2), (1, 6)], [32, 32, 16]),   # largest piece can stay the same
        (3, 7, [(0, 6), (0, 1)], [18, 15]),
    ]

    for i, (w, h, cuts, expected) in enumerate(tests, 1):
        result = largest_area(w, h, cuts)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        if status == "FAIL":
            print(f"  w={w}, h={h}, cuts={cuts}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")