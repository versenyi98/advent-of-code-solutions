import sys

def main():
    task1 = [line.strip('\n').split(': ')[-1] for line in sys.stdin.readlines()]
    task2 = [line.replace(' ', '') for line in task1]

    for task in [task1, task2]:
        result = 1
        for length, record in zip(task[0].split(), task[1].split()):
            length = int(length)
            record = int(record)

            ways = 0
            for speed in range(length):
                if speed * (length - speed) > record:
                    ways += 1
            result *= ways
        print(result)

if __name__ == "__main__":
    main()