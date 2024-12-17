import sys
from z3 import Optimize, BitVec, BitVecVal

def get_combo(registers, combo):
  if 0 <= combo <= 3:
    return combo
  if combo == 4:
    return registers[0]
  if combo == 5:
    return registers[1]
  if combo == 6:
    return registers[2]

def task1(registers, operations):
  i = 0
  result = []
  while i < len(operations):
    operation = operations[i]
    step = 2
    if operation == 0:
      numerator = registers[0]
      denominator = 2 ** get_combo(registers, operations[i + 1])
      registers[0] = numerator // denominator
    elif operation == 1:
      registers[1] = registers[1] ^ operations[i + 1]
    elif operation == 2:
      registers[1] = get_combo(registers, operations[i + 1]) % 8
    elif operation == 3:
      if registers[0] != 0:
        i = operations[i + 1]
        step = 0
    elif operation == 4:
      registers[1] = registers[1] ^ registers[2]
    elif operation == 5:
      result.append(get_combo(registers, operations[i + 1]) % 8)
    elif operation == 6:
      numerator = registers[0]
      denominator = 2 ** get_combo(registers, operations[i + 1])
      registers[1] = numerator // denominator
    elif operation == 7:
      numerator = registers[0]
      denominator = 2 ** get_combo(registers, operations[i + 1])
      registers[2] = numerator // denominator
    i += step

  return result

def task2(operations):
  # hard coded optimizer for input
  optimizer = Optimize()

  A = [BitVec(f'A_{i}', 64) for i in range(len(operations) + 1)]
  B = [BitVec(f'B_{i}', 64) for i in range(len(operations) + 1)]
  C = [BitVec(f'C_{i}', 64) for i in range(len(operations) + 1)]

  for i, operation in enumerate(operations, 1):
    optimizer.add(C[i] == A[i - 1] >> ((A[i - 1] % 8) ^ BitVecVal(7, 64)))
    optimizer.add(B[i] == ((A[i - 1] % 8) ^ C[i]))
    optimizer.add(A[i] == A[i - 1] >> 3)
    optimizer.add(B[i] % 8 == operation)
    if i == len(operations):
      optimizer.add(A[i] == 0)
    else:
      optimizer.add(A[i] > 0)

  optimizer.add(B[0] == 0)
  optimizer.add(C[0] == 0)
  optimizer.minimize(A[0])

  optimizer.check()

  return optimizer.model()[A[0]]

def main():
  registers, operations = sys.stdin.read().split('\n\n')
  registers = [int(register.split(':')[-1]) for register in registers.split('\n')]
  operations = list(map(int, operations.split(': ')[-1].split(',')))

  print(",".join(map(str, task1(registers.copy(), operations.copy()))))
  print(task2(operations))

if __name__ == "__main__":
    main()