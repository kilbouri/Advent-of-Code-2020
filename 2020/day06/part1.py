from os import getcwd


def main():
    with open(f"{getcwd()}/2020/day06/input.txt", "r") as input:
        groups = input.read().split("\n\n")

    count = 0
    for group in groups:
        answers = set(group)

        if "\n" in answers:
            answers.remove("\n")

        count += len(answers)
    print(count)


if __name__ == "__main__":
    main()
