# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    Stuart_result = 0
    Kevin_result = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            Kevin_result += length - i
        else:
            Stuart_result += length - i

    if Stuart_result > Kevin_result:
        print(f"Stuart {Stuart_result}")
    elif Stuart_result < Kevin_result:
        print(f"Kevin {Kevin_result}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

# Stuart - START!! suglasni
# Kevin - glasni
