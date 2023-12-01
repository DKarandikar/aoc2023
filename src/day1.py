
numbers = "1234567890"

text_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}


def get_first_number(s: str, with_str: bool = False, reverse: bool = False):
    acc = ""
    for x in (s[::-1] if reverse else s):
        acc += x
        if x in numbers:
            return x
        if with_str:
            for k in text_map:
                if (not reverse and k in acc) or (reverse and k[::-1] in acc):
                    return text_map[k]
    raise RuntimeError(f"Invalid line: {s}")


def extract_first_last_number(s: str, with_str: bool = False) -> int:
    first = get_first_number(s, with_str)
    last = get_first_number(s, with_str, True)

    return int(first + last)


def main():
    with open("../data/day1.txt") as f:
        lines = f.readlines()

    print(f"Part 1 answer is: {sum([extract_first_last_number(l) for l in lines])}")
    print(f"Part 2 answer is: {sum([extract_first_last_number(l, True) for l in lines])}")


if __name__ == '__main__':
    main()
