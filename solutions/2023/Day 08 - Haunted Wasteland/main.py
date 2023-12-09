import sys
from math import lcm

def simulate(start_states, instructions, transitions, is_goal_state):
    results = [0] * len(start_states)

    for i, state in enumerate(start_states):
        while not is_goal_state(state):
            if instructions[results[i] % len(instructions)] == 'L':
                state = transitions[state][0]
            else:
                state = transitions[state][1]
            results[i] += 1

    return lcm(*results) # not sure about this one

def task1(instructions, transitions):
    def is_goal_state(state):
        return state == 'ZZZ'

    return simulate(['AAA'], instructions, transitions, is_goal_state)

def task2(instructions, transitions):
    def is_goal_state(state):
        return state[-1] == 'Z'

    start_states = [state for state in transitions if state[-1] == 'A']

    return simulate(start_states, instructions, transitions, is_goal_state)


def main():
    instructions = sys.stdin.readline().strip('\n')
    lines = [line.strip("\n").replace("(", "").replace(")", "").split(" = ") for line in sys.stdin.readlines()[1:]]
    transitions = {line[0]: line[1].split(', ') for line in lines}

    print(task1(instructions, transitions))
    print(task2(instructions, transitions))

if __name__ == "__main__":
    main()