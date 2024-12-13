import sys
import collections
import re
import math

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

def get_variables(x, y, z):
  (x1, y1), (x2, y2), (x3, y3) = x, y, z

  common_coefficient = lcm(x1, y1)
  f1 = common_coefficient // x1
  f2 = common_coefficient // y1
  x1, x2, x3 = x1 * f1, x2 * f1, x3 * f1
  y1, y2, y3 = y1 * f2, y2 * f2, y3 * f2

  A, B = 0, 0

  if (y3 - x3) % (y2 - x2) == 0:
    B = (y3 - x3) // (y2 - x2)
    if (x3 - B * x2) % x1 == 0:
      A = (x3 - B * x2) // x1

  return A, B

def main():
  testcases = [testcase.split('\n') for testcase in sys.stdin.read().split('\n\n')]
  pattern = r"(\d+)"

  testcases = [tuple(map(int, re.findall(pattern, line))) for testcase in testcases for line in testcase]
  for extra in [0, 10000000000000]:
    result = 0
    for i in range(0, len(testcases), 3):
      (x1, x2), (y1, y2), (z1, z2) = testcases[i:i+3]
      z1, z2 = z1 + extra, z2 + extra
      A, B = get_variables((x1, x2), (y1, y2), (z1, z2))

      if A * x1 + B * y1 == z1 and A * x2 + B * y2 == z2 and A >= 0 and B >= 0:
        result += A * 3 + B

    print(result)

if __name__ == "__main__":
    main()