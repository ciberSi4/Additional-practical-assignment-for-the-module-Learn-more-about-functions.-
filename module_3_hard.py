res : int = 0

def calculate_structure_sum (*args):
    global res

    for i in args:
        if isinstance(i, int):
            res += i
        elif len(i) >= 1: # not(len (i) == 0):
            if isinstance(i, str):
                res += len(i)
            elif isinstance(i, dict):
                calculate_structure_sum(*i.keys())
                calculate_structure_sum(*i.values())
            elif isinstance(i, list):
                calculate_structure_sum (*i)
            elif isinstance(i, tuple):
                calculate_structure_sum(*i)
            elif isinstance(i, set):
                list_ : list = list (i)
                calculate_structure_sum(*list_)
        else:
            continue

    return res


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(f"Сумма всех чисел и длин всех строк: {result}")