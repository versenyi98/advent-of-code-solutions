import sys

def task(target, ops, allow_concat):
    def rec(curr, i):
        if curr > target:
            return 0
        if i == len(ops):
            return target if target == curr else 0
        if rec(curr + ops[i], i + 1):
            return target
        if rec(curr * ops[i], i + 1):
            return target
        if allow_concat and rec(int(str(curr) + str(ops[i])), i + 1):
            return target
        return 0
    return rec(0, 0)

def main():
    lines = [line.split(': ') for line in sys.stdin.read().split('\n')]
    lines = [(int(target), list(map(int, operands.split()))) for target, operands in lines]
    
    print(sum(task(target, operands, False) for target, operands in lines))
    print(sum(task(target, operands, True) for target, operands in lines))
    
if __name__ == "__main__":
    main()