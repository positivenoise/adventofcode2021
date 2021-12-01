def how_many_increments_by_average(numbers, average_len=3):
    initial_sum_measurement = sum(numbers[0:average_len])
    result = 0

    for x in range(average_len, len(numbers) + 1):
        s = sum(numbers[x-average_len:x])
        if s > initial_sum_measurement:
            result += 1
        initial_sum_measurement = s

    return result

lines = open("data.txt").read().splitlines()

numbers = [int(x) for x in lines]

result = how_many_increments_by_average(numbers)

print(result)

