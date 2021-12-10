
def exerciseone(input):
    count = 0
    for x, y in zip(input, input[1:]):
        if count > 1450:
            print(x)
            print(y)
            print(count)
        if x < y:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as file1:
        print("The answer to the first: " + str(exerciseone(file1.readlines())))

