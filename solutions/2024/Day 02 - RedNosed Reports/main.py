import sys
import collections

def is_safe_dec(seq):
  return all(0 < seq[i] - seq[i + 1] < 4 for i in range(len(seq) - 1))

def is_safe_inc(seq):
  return all(0 < seq[i + 1] - seq[i] < 4 for i in range(len(seq) - 1))

def is_safe(seq):
  return is_safe_dec(seq) or is_safe_inc(seq)

def task1(seqs):
  return sum(1 if is_safe(seq) else 0 for seq in seqs)

def task2(seqs):
  def is_safe_with_removal(seq):
    if is_safe(seq):
      return True

    for i in range(len(seq)):
      new_seq = seq[:i] + seq[i + 1:]
      if is_safe(new_seq):
        return True
    return False

  return sum(1 if is_safe_with_removal(seq) else 0 for seq in seqs)

def main():
  lines = sys.stdin.read().split('\n')
  lines = [list(map(int, line.split())) for line in lines]

  print(task1(lines))
  print(task2(lines))

if __name__ == "__main__":
  main()