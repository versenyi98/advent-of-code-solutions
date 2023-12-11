import sys

def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    transposed = ["".join(col) for col in zip(*[iter(row) for row in lines])]

    row_has_galaxy = [line.find('#') != -1 for line in lines]
    col_has_galaxy = [line.find('#') != -1 for line in transposed]

    galaxies = []

    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == '#':
                galaxies.append((r, c))

    task1 = 0
    task2 = 0
    for galaxy_a in galaxies:
        for galaxy_b in galaxies:
            if galaxy_a == galaxy_b:
                continue

            step_r = 1 if galaxy_a[0] < galaxy_b[0] else -1
            step_c = 1 if galaxy_a[1] < galaxy_b[1] else -1

            for row in range(galaxy_a[0] + step_r, galaxy_b[0] + step_r, step_r):
                task1 += 1 if row_has_galaxy[row] else 2
                task2 += 1 if row_has_galaxy[row] else 1000000
            for col in range(galaxy_a[1] + step_c, galaxy_b[1] + step_c, step_c):
                task1 += 1 if col_has_galaxy[col] else 2
                task2 += 1 if col_has_galaxy[col] else 1000000

    print(task1 // 2)
    print(task2 // 2)

if __name__ == "__main__":
    main()