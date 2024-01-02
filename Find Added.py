# https://www.codewars.com/kata/58de77a2c19f096a5a00013f/train/python

def find_added(st1, st2):
    result, st1, st2 = list(), sorted(st1), sorted(st2)

    for i in range(len(st2)):
        if not st2[i] in st1:
            result.append(st2[i])
        else:
            st1.remove(st2[i])

    return "".join(result)


print(find_added('4455446', '447555446666'))
print(find_added('44554466', '447554466'))
print(find_added('9876521', '9876543211'))
print(find_added('678', '876'))
print(find_added('678', '6'))
