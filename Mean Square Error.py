# https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python

def solution(array_a, array_b):
    square = []
    for x in range(len(array_a)):
        square.append(abs(array_a[x] - array_b[x]) ** 2)

    total_square = sum(square)
    avg = total_square / len(array_a)
    return avg


print(solution([1, 2, 3], [4, 5, 6]))
print(solution([10, 20, 10, 2], [10, 25, 5, -2]))
print(solution([-1, 0], [0, -1]))
