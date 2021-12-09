
def exercisetwo(input):
    horizontal = 0
    depth = 0
    for item in input:
        direction, amount = item.split()
        if direction == "forward":
            horizontal += int(amount)
        elif direction == "up":
            depth -= int(amount)
        elif direction == "down":
            depth += int(amount)
        else:
            return -1, -1
    return str(horizontal * depth)


if __name__ == "__main__":
    with open("input.txt", "r") as file1:
        print("The answer to the second exercise is: " + exercisetwo(file1.readlines()))

