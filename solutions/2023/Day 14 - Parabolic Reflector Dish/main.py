import sys

def tilt(lines, direction):
    dr, dc = direction

    row_range = range(len(lines)) if dr <= 0 else range(len(lines) - 1, -1, -1)
    col_range = range(len(lines[0])) if dc <= 0 else range(len(lines[0]) - 1,  -1, -1)

    for row_num in row_range:
        for col_num in col_range:
            if lines[row_num][col_num] != 'O':
                continue

            r = row_num
            c = col_num

            while r + dr >= 0 and r + dr < len(lines) and c + dc >= 0 and c + dc < len(lines[0]) and lines[r + dr][c + dc] == '.':
                nr = r + dr
                nc = c + dc

                lines[r] = lines[r][:c] + '.' + lines[r][c + 1:]
                lines[nr] = lines[nr][:nc] + 'O' + lines[nr][nc + 1:]
                r += dr
                c += dc

def count_result(lines):
    result = 0

    for r, row in enumerate(lines):
        for col in row:
            result += (len(lines) - r) if col == 'O' else 0
    return result

def main():
    lines = [line.strip('\n') for line in sys.stdin.readlines()]
    results = []

    limit = 1000000000
    fast_forwarded = False
    round = 0

    while round < limit:
        result = []

        for tilt_direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            tilt(lines, tilt_direction)
            result.append(count_result(lines))

            if round == 0 and len(result) == 1:
                print(result[0])

        if not fast_forwarded and results.count(result) == 1:
            fast_forwarded = fast_forwarded
            cycle_len = round - results.index(result)

            cycles = (limit - round) // cycle_len
            round += cycle_len * cycles
        else:
            round += 1
        results.append(result)

    print(results[-1][-1])

if __name__ == "__main__":
    main()