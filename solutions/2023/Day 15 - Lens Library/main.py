import sys

def hash(label):
    current = 0
    for ch in label:
        current += ord(ch)
        current *= 17
        current %= 256
    return current

def main():
    strings = sys.stdin.readline().split(',')

    print(sum([hash(string) for string in strings]))

    mapping = {}
    boxes = [[] for _ in range(256)]

    for string in strings:
        if '-' in string:
            string = string[:-1]
            if string in mapping:
                old_value = mapping[string]

                i = hash(string)
                j = boxes[i].index(old_value)

                boxes[i] = boxes[i][:j] + boxes[i][j + 1:]
                del mapping[string]
        else:
            sign = string.index('=')

            num = int(string[sign + 1:])
            string = string[:sign]

            if string in mapping:
                value = mapping[string]
                i = hash(string)
                j = boxes[i].index(value)

                boxes[i] = boxes[i][:j] + [(string, num)] + boxes[i][j + 1:]
            else:
                boxes[hash(string)].append((string, num))
            mapping[string] = (string, num)

    print(sum([b * s * focal for b, box in enumerate(boxes, 1) for s, (_, focal) in enumerate(box, 1)]))

if __name__ == "__main__":
    main()