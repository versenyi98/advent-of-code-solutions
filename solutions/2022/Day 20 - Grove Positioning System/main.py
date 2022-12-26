import sys


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.prev.value} <- {self.value} -> {self.next.value}"


test_cases = [list(map(int, test_case.split("\n"))) for test_case in sys.stdin.read().split("\n\n")]


def print_list(head, length):
    for i in range(length):
        print(head.value, end=" ")
        head = head.next
    print()


def solve(part):
    for test_case in test_cases:
        original = [(idx, val * (811589153 if part == 2 else 1)) for idx, val in enumerate(test_case)]
        prev = None
        zero_node = None
        nodes = {}

        for entry in original:
            node = Node(entry[1], None, None)
            if entry[1] == 0:
                zero_node = node
            if prev:
                nodes[prev].next = node
                node.prev = nodes[prev]
            prev = entry

            nodes[entry] = node

        nodes[original[0]].prev = nodes[original[-1]]
        nodes[original[-1]].next = nodes[original[0]]

        max_round = 1 if part == 1 else 10
        for round_no in range(1 if part == 1 else 10):
            for idx, entry in enumerate(original):
                if (idx + 1) % 100 == 0:
                    print(f"\rRound {round_no + 1}/{max_round}: {idx + 1}/{len(test_case)}", end="")
                node = nodes[entry]
                value = node.value % (len(original) - 1)

                while value != 0:
                    if value < 0:
                        prev = node.prev
                        prev_prev = prev.prev
                        next = node.next

                        prev.next = next
                        prev.prev = node
                        next.prev = prev

                        node.next = prev
                        node.prev = prev_prev
                        prev_prev.next = node

                        value += 1
                    if value > 0:
                        next = node.next
                        next_next = next.next
                        prev = node.prev

                        next.next = node
                        next.prev = prev
                        prev.next = next

                        node.prev = next
                        node.next = next_next
                        next_next.prev = node

                        value -= 1
        head = zero_node
        result = 0
        for counter in range(3000):
            head = head.next
            if counter % 1000 == 999:
                result += head.value
        print(f"\r{result}" + " " * 100)


solve(1)
print()
solve(2)