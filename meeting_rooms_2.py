def min_meeting_rooms(intervals: list[list[int]]) -> int:
    start =[]
    end= []
    max_rooms = 0
    start = sorted(iv[0] for iv in intervals)
    end = sorted(iv[1] for iv in intervals)
    s = 0
    e = 0
    rooms = 0
    while s < len(intervals):
        if start[s] < end[e]:
            rooms += 1
            s += 1
        else: 
            rooms -= 1
            e +=1
        max_rooms = max(max_rooms, rooms)
    return max_rooms
        
        


                
if __name__ == "__main__":
    tests = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([], 0),
        ([[1, 5]], 1),
        ([[1, 5], [5, 10]], 1),                 # touching: can share a room
        ([[1, 5], [5, 10], [10, 15]], 1),       # chain of touching meetings
        ([[1, 10], [2, 9], [3, 8], [4, 7]], 4), # all nested
        ([[5, 7], [1, 10], [2, 3]], 2),         # unsorted input
        ([[1, 4], [2, 5], [3, 6], [4, 7]], 3),  # peak of 3, then [1,4] frees for [4,7]
        ([[1, 2], [1, 2], [1, 2]], 3),          # identical meetings
    ]

    for i, (intervals, expected) in enumerate(tests, 1):
        result = min_meeting_rooms([iv[:] for iv in intervals])
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        if status == "FAIL":
            print(f"  input:    {intervals}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")