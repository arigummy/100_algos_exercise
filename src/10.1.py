data = "sd(asd[ad]{sda)})s"

stack = []

pairs = {'(': ')', '[': ']', '{': '}'}

correct_state = True

for char in data:

    if char in pairs.keys():
        stack.append(char)
    elif char in pairs.values():
        # if not stack:
        #     correct_state = False
        #     break
        # top = stack.pop()
        # print(f"Pop: {top}")
        if char != pairs.get(stack.pop()):
            correct_state = False
            break
    # print(char, end=' ')
    # print(stack)

print(correct_state)
