from os.path import dirname


def main():
    sum = 0
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        for mass in input:
            # first line is 74159 given input 148319
            sum += int(mass) // 3 - 2

    print(sum)


if __name__ == "__main__":
    main()
