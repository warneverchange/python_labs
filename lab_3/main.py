from functools import reduce
import csv


with open('dataset.csv') as csv_file:
    rows = csv.reader(csv_file, delimiter=",")
    years = list(map(lambda date: int(date[:4]), [row[1] for row in rows][1:]))

    print(f"Years: {sorted(set(years))}")

    print("Enter start year: ", end='')
    _from = int(input())
    print("Enter end year: ", end='')
    _to = int(input())

    if _to not in years or _from not in years:
        exit(1)

    csv_file.seek(0)
    values = list(map(float, [row[2] if row[2] != '' else 0 for row in rows][1:]))
    result: dict = dict()
    for i in range(len(years)):
        if years[i] not in result:
            result[years[i]] = values[i]
        else:
            result[years[i]] += values[i]

    def get_sum(prev_sum: tuple, curr_val: tuple) -> tuple:
        return prev_sum[0], prev_sum[1] + curr_val[1]


    print("Sum of values: ", end='')
    _sum = round(reduce(get_sum, list(filter(lambda item: _from <= item[0] <= _to, result.items())))[1], 2)
    print(_sum)


