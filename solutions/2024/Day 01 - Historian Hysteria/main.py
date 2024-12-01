import sys
import collections

def task1(list1, list2):
    return sum(abs(num1 - num2) for num1, num2 in zip(sorted(list1), sorted(list2)))

def task2(list1, list2):
    counter = collections.Counter(list2)
    return sum(num * counter[num] for num in list1)

def main():
    lines = sys.stdin.read().split('\n')
    list1, list2 = zip(*[map(int, line.split()) for line in lines])

    print(task1(list1, list2))
    print(task2(list1, list2))

if __name__ == "__main__":
    main()