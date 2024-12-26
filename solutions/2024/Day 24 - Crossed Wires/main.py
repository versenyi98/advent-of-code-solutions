import sys

def get_value(variable, variables, rules):
    if variable in variables:
        return variables[variable]

    rule = rules[variable]

    val1 = get_value(rule[0], variables, rules)
    val2 = get_value(rule[2], variables, rules)

    if rule[1] == 'AND':
        variables[variable] = 1 if val1 == 1 and val2 == 1 else 0
    elif rule[1] == 'OR':
        variables[variable] = 1 if val1 == 1 or val2 == 1 else 0
    elif rule[1] == 'XOR':
        variables[variable] = 1 if val1 != val2 else 0
    return variables[variable]

def task1(variables):
    results = []
    for v in variables:
        if v.startswith("z"):
            results.append((v, variables[v]))
    result = 0
    for r in sorted(results):
        result += pow(2, int(r[0][1:])) if r[1] else 0
    print(result)

def get_rules_rec(variable, rules, depth=0):
    if depth > 2:
        return
    if variable in rules:
        op1, op2, op3 = rules[variable]
        print(f"{variable} = {op1} {op2} {op3}")

        get_rules_rec(op1, rules, depth + 1)
        get_rules_rec(op3, rules, depth + 1)

def check_rule(number, rules):
    x = f'x{number:02}'
    y = f'y{number:02}'
    z = f'z{number:02}'

    xp = f'x{number - 1:02}'
    yp = f'y{number - 1:02}'
    zp = f'z{number - 1:02}'

    xor_x_y =  [(name, rule) for name, rule in rules.items() if rule[1] == 'XOR' and rule[0] in [x, y] and rule[2] in [x, y]][0]
    and_prev = [(name, rule) for name, rule in rules.items() if rule[1] == 'AND' and rule[0] in [rules[zp][0], rules[zp][2]] and rule[2] in [rules[zp][0], rules[zp][2]]][0]
    and_px_py = [(name, rule) for name, rule in rules.items() if rule[1] == 'AND' and rule[0] in [xp, yp] and rule[2] in [xp, yp]][0]
    or_ = [(name, rule) for name, rule in rules.items() if rule[1] == 'OR' and rule[0] in [and_px_py[0], and_prev[0]] and rule[2] in [and_prev[0], and_px_py[0]]][0]

    main_rule = (z, rules[z])
    main_rule_calc = [(name, rule) for name, rule in rules.items() if rule[1] == 'XOR' and rule[0] in [xor_x_y[0], or_[0]] and rule[2] in [xor_x_y[0], or_[0]]]

    if len(main_rule_calc) and main_rule != main_rule_calc[0]:
        main_rule_calc = main_rule_calc[0]
        rules[main_rule[0]], rules[main_rule_calc[0]] = rules[main_rule_calc[0]], rules[main_rule[0]]
        return [main_rule[0], main_rule_calc[0]]
    elif xor_x_y[0] not in [rules[z][0], rules[z][2]]:
        if or_[0] == rules[z][2]:
            rules[rules[z][0]], rules[xor_x_y[0]] = rules[xor_x_y[0]], rules[rules[z][0]]
            return [rules[z][0], xor_x_y[0]]
        else:
            rules[rules[z][2]], rules[xor_x_y[0]] = rules[xor_x_y[0]], rules[rules[z][2]]
            return [rules[z][2], xor_x_y[0]]
    return []

def main():
    initial, raw_rules = sys.stdin.read().split('\n\n')
    initial = [init.split(': ') for init in initial.split('\n')]
    raw_rules = [rule.split(' ') for rule in raw_rules.split('\n')]

    rules = {}
    variables = {}

    for rule in raw_rules:
        rules[rule[-1]] = (rule[0], rule[1], rule[2])

    for variable, value in initial:
        variables[variable] = int(value)

    for v in rules:
        get_value(v, variables, rules)

    print(task1(variables))

    flipped = []
    for i in range(2, 45):
        flipped += check_rule(i, rules)
    print(','.join(sorted(flipped)))

if __name__ == "__main__":
    main()