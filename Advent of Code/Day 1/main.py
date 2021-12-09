
def exerciseone(input):
    count = 1
    for i in range(len(input)-1):
        if input[i] < input[i+1]:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as file1:
        print("The answer to the first: " + str(exerciseone(file1.readlines())))

