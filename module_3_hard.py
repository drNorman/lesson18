def calculate_structure_sum(*args):
    sum = 0
    for i in range(len(args)):

        if isinstance(args[i], dict):
            for k, v in args[i].items():
                sum += calculate_structure_sum(k)
                sum += calculate_structure_sum(v)
        elif isinstance(args[i], tuple | list | set):
            for j in args[i]:
                sum += calculate_structure_sum(j)
        elif isinstance(args[i], str):
            sum += len(args[i])
        elif isinstance(args[i], int):
            sum += args[i]
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
