import sys

rows, cols = 0, 0
lines = []

def in_range(r, c):
  return (0 <= r < rows) and (0 <= c < cols)

def is_mas(pos):
  r, c = pos
  diags = [[(r - 1, c - 1), (r + 1, c + 1)],
           [(r - 1, c + 1), (r + 1, c - 1)]]

  return lines[r][c] == 'A' and \
      all(all(in_range(nr, nc) for nr, nc in diag) for diag in diags) and \
      all(any(lines[nr][nc] == 'M' for nr, nc in diag) for diag in diags) and \
      all(any(lines[nr][nc] == 'S' for nr, nc in diag) for diag in diags)

def count_of_words_from_pos(pos):
  r, c = pos
  words = ["".join(
            [lines[r + n * dr][c + n * dc] 
            for n in range(4) 
            if in_range(r + n * dr, c + n * dc)]
          )
          for dr in range(-1, 2)
          for dc in range(-1, 2)]
  return words.count('XMAS')

def main():
  global lines, rows, cols

  lines = sys.stdin.read().split('\n')

  rows = len(lines)
  cols = len(lines[0])

  pairs = list((i, j) for i in range(rows) for j in range(cols))
  print(sum(map(count_of_words_from_pos, pairs)))
  print(sum(map(is_mas, pairs)))

if __name__ == "__main__":
    main()