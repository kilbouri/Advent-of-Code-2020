from os import getcwd


def main():
    with open(f"{getcwd()}/2020/day01/input.txt", "r") as input:
        numbers = set(map(int, map(str.strip, input.readlines())))

        for number in numbers:
            for number2 in numbers:
                if 2020 - number - number2 in numbers:
                    product = number * number2 * (2020 - number - number2)
                    print("Found: " + str(2020 - number - number2) +
                          " * " + str(number) + " * " + str(number2) +
                          " = " + str(product))
                    exit()


if __name__ == "__main__":
    main()
