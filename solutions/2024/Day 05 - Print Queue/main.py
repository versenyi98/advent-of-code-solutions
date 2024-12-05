import sys
import collections

def get_problem(order, rules):
  for i, number in enumerate(order):
    intersection = list(set(rules[number]) & set(order[:i]))

    if intersection:
      return order.index(intersection[-1]), i
  return None

def task1(rules, orders):
  return sum(o[len(o)//2] for o in orders if get_problem(o, rules) is None)

def task2(rules, orders):
  def fix(order):
    while (problem := get_problem(order, rules)) is not None:
      i, j = problem
      order[i], order[j] = order[j], order[i]
    return order

  bad_orders = [o for o in orders if get_problem(o, rules) is not None]
  return sum(o[len(o) // 2] for o in map(fix, bad_orders))

def main():
  input_ = sys.stdin.read().split('\n\n')
  orders = [list(map(int, o.split(','))) for o in input_[1].split('\n')]

  rules = collections.defaultdict(list)
  for rule in input_[0].split('\n'):
    key, value = map(int, rule.split('|'))
    rules[key].append(value)

  print(task1(rules, orders))
  print(task2(rules, orders))

if __name__ == "__main__":
  main()