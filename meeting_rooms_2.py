def min_meeting_rooms(intervals: list[list[int]]) -> int:
    start = []
    for i in range(len(intervals)):
        start.append(intervals[i][0])
    start.sort()

    end = []
    for i in range(len(intervals)):
        end.append(intervals[i][1])
    end.sort()

    i = 0
    j=0
    rooms = 0
    max_rooms = 0
    
    print(start)
    print(end)
    # if len(intervals) == 1:
    #     return 1
    while i < len(intervals):
        if start[i] < end[j]:
            i += 1
            rooms +=1
        elif start[i] == end[j]:
            i+=1
            j+=1
        else:
            j+=1
            rooms -=1
        
        # elif start[i] > end[i]:
        #     j+=1
        #     rooms -=1
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