def how_many_increments(numbers):
    prev_num = numbers[0]
    result = 0

    for num in numbers:
        if num > prev_num:
            result += 1
        prev_num = num

    return result

lines = open("data.txt").read().splitlines()

numbers = [int(x) for x in lines]

result = how_many_increments(numbers)

print(result)

