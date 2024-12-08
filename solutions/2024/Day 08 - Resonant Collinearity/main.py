import sys
import collections

rows, cols = 0, 0

def task(antennas, times):
  antinode_positions = set([
    (x, y)
     for positions in antennas.values()
     for (x1, y1) in positions
     for (x2, y2) in positions
     for t in times
     if (x1, y1) != (x2, y2) and 
        0 <= (x := x1 + t * (x1 - x2)) < rows and
        0 <= (y := y1 + t * (y1 - y2)) < cols
  ])

  return len(antinode_positions)

def main():
  global rows, cols

  lines = sys.stdin.read().split('\n')
    
  rows = len(lines)
  cols = len(lines[0])
        
  antennas = collections.defaultdict(list)
      
  for row, line in enumerate(lines):
    for col, ch in enumerate(line):
      if ch != '.':
        antennas[ch].append((row, col))

  print(f"Task 1: {task(antennas, range(1, 2))}")
  print(f"Task 2: {task(antennas, range(0, rows + 1))}")
    
if __name__ == "__main__":
    main()