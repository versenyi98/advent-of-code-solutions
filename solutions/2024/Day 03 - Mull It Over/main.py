import sys
import re
import math

allow = True

def mul(x, y):
    return x * y if allow else 0

def do():
    global allow
    allow = True
    return 0

def dont():
    global allow
    allow = False
    return 0

def task1(line):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, line)
    return sum(eval(m) for m in matches)

def task2(line):
    pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, line)
    matches = ["dont()" if m == "don't()" else m for m in matches]

    return sum(eval(m) for m in matches)

def main():
    line = "".join(sys.stdin.read().split('\n'))

    print(task1(line))
    print(task2(line))

if __name__ == "__main__":
    main()