# https://www.hackerrank.com/challenges/text-wrap/problem


import textwrap


def wrap(string, max_width):
    output = []

    for x in range(0, len(string), max_width):
        output.append(string[:max_width])
        string = string[max_width:]

    return "\n".join(output)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
