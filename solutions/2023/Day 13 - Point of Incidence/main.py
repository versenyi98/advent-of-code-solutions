import sys

def diff(original, mirrored):
    return sum([1 for o, m in zip(original, mirrored) for oo, mm in zip(o, m) if oo != mm])

def find_mirror(group, smudge):
    for r in range(len(group)):
        original = group[:r]
        mirrored = group[r:]
        length = min(len(original), len(mirrored))

        original = original[-length:]
        mirrored = mirrored[:length]

        if length and diff(original, mirrored[::-1]) == smudge:
            return r
    return -1

def main():
    lines = [[line for line in group.split('\n')] for group in sys.stdin.read().split('\n\n') ]

    for task in range(2):
        results = []

        for group in lines:
            if (mirror_pos := find_mirror(group, task)) != -1:
                results.append(100 * mirror_pos)
            else:
                rotated = ["".join(col) for col in zip(*[iter(row) for row in group])]
                results.append(find_mirror(rotated, task))
        print(sum(results))

if __name__ == "__main__":
    main()