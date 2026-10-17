def process_commands(commands: list[str]) -> list[str]:
    stack = []
    for i in commands:
        command = i.split(" ")
        if command[0] == "open":
            stack.append(command[1])
        elif command[0] == "close":
            for j in range(int(command[1])):
                if len(stack) >=1:
                    stack.pop()
        else:
            stack = []

    return stack

if __name__ == "__main__":
    tests = [
        # (commands, expected)
        (["open chrome", "open slack", "open zoom", "close 2", "open spotify"],
         ["chrome", "spotify"]),
        ([], []),
        (["open a"], ["a"]),
        (["open a", "open b", "close 5"], []),            # k > open count
        (["clear"], []),                                  # clear on empty
        (["close 1"], []),                                # close on empty
        (["open a", "open b", "clear", "open c"], ["c"]),
        (["open a", "open a", "close 1"], ["a"]),          # duplicates allowed
        (["open a", "open b", "open c", "close 0"], ["a", "b", "c"]),  # close 0
        (["open x", "open y", "close 1", "close 1", "open z"], ["z"]),
    ]

    for i, (cmds, expected) in enumerate(tests, 1):
        result = process_commands(cmds)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        if status == "FAIL":
            print(f"  commands: {cmds}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")