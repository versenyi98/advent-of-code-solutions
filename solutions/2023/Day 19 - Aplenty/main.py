import sys
import math

def process_cond(cond):
    colon = cond.find(':')
    comma = cond.find(',')

    if colon == -1:
        return [[branch] for branch in cond.split(',')]

    if colon < comma:
        result = [cond.split(':')[0], process_cond(":".join(cond.split(':')[1:]))]
    else:
        result = [[cond.split(',')[0]], process_cond(','.join(cond.split(',')[1:]))]
    return result

def process_func(func):
    begin = func.find('{')

    name = func[:begin]
    cond = func[begin + 1:-1]

    return name, process_cond(cond)

def task1(func_map, func, parts):
    if func[0].find('>') == -1 and func[0].find('<') == -1:
        if func[0] in func_map:
            return task1(func_map, func_map[func[0]], parts)
        elif func[0] == 'A':
            return sum(parts.values())
        else:
            return 0

    if func[0].find('>') != -1:
        char, number = func[0].split('>')
        return task1(func_map, func[1][0 if parts[char] > int(number) else 1], parts)
    elif func[0].find('<') != -1:
        char, number = func[0].split('<')
        return task1(func_map, func[1][0 if parts[char] < int(number) else 1], parts)

def task2(func_map, func, parts):
    if func[0].find('>') == -1 and func[0].find('<') == -1:
        if func[0] in func_map:
            return task2(func_map, func_map[func[0]], parts)
        elif func[0] == 'A':
            return math.prod([upper - lower for lower, upper in parts.values() if upper > lower])
        else:
            return 0

    parts_1 = parts.copy()
    parts_2 = parts.copy()

    if func[0].find('>') != -1:
        char, number = func[0].split('>')
        number = int(number)

        parts_1[char] = [max(parts_1[char][0], number), parts_1[char][1]]
        parts_2[char] = [parts_2[char][0], min(parts_2[char][1], number)]

    elif func[0].find('<') != -1:
        char, number = func[0].split('<')
        number = int(number)

        parts_1[char] = [parts_1[char][0], min(parts_1[char][1], number - 1)]
        parts_2[char] = [max(number - 1, parts_2[char][0]), parts_2[char][1]]

    return task2(func_map, func[1][0], parts_1) + \
        task2(func_map, func[1][1], parts_2)

def main():
    funcs, parts = sys.stdin.read().split("\n\n")
    func_map = {}

    for func in funcs.split('\n'):
        name, cond = process_func(func)
        func_map[name] = cond

    parts = parts.split('\n')

    for i, part in enumerate(parts):
        values = part[1:-1].split(',')
        parts[i] = {k: int(v) for k, v in map(lambda x : x.split('='), values)}

    in_func = func_map['in']

    print(sum([task1(func_map, in_func, part) for part in parts]))
    print(task2(func_map, in_func, {k: [0, 4000] for k in "xmas"}))


if __name__ == "__main__":
    main()