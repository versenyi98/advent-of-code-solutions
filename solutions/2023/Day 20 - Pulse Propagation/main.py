import sys
import math

def main():
    flip_flops = {}
    conjunctions = {}
    broadcaster = None

    lines = [line.strip('\n') for line in sys.stdin.readlines()]

    for line in lines:
        if line[0] == '&':
            # conjunctions
            name, connections = line[1:].split(' -> ')
            conjunctions[name] = [{}, connections.split(', ')]

    for line in lines:
        if line[0] == '%':
            # flip flop
            name, connections = line[1:].split(' -> ')
            flip_flops[name] = [False, connections.split(', ')]

            for conn in flip_flops[name][1]:
                if conn in conjunctions:
                    conjunctions[conn][0][name] = False
        elif line[0] == 'b':
            # broadcaster
            name, connections = line[1:].split(' -> ')
            broadcaster = connections.split(', ')

            for conn in broadcaster:
                if conn in conjunctions:
                    conjunctions[conn][0][name] = False


    lows = 0
    highs = 0

    high_signal_sent = {}

    button_presses = 0

    while len(high_signal_sent) != 4 or not all([len(values) >= 2 for values in high_signal_sent.values()]):
        button_presses += 1
        lows += len(broadcaster) + 1
        queue = [(False, conn) for conn in broadcaster]

        while len(queue):
            head = queue.pop(0)
            is_high, node = head


            # based on my input, inputs for 'gf' which is the only input for 'rx'
            if node in ['sp', 'pg', 'sv', 'qs'] and not all(conjunctions[node][0].values()):
                if node not in high_signal_sent:
                    high_signal_sent[node] = []
                if len(high_signal_sent[node]) < 2:
                    high_signal_sent[node].append(button_presses)

            if node in flip_flops:
                if is_high:
                    continue

                flip_flops[node][0] = not flip_flops[node][0]
                queue += [(flip_flops[node][0], conn) for conn in flip_flops[node][1]]

                if flip_flops[node][0]:
                    highs += len(flip_flops[node][1])
                else:
                    lows += len(flip_flops[node][1])

                for conn in flip_flops[node][1]:
                    if conn in conjunctions:
                        conjunctions[conn][0][node] = flip_flops[node][0]

            elif node in conjunctions:
                # not all high
                if not all(conjunctions[node][0].values()):
                    queue += [(True, conn) for conn in conjunctions[node][1]]

                    highs += len(conjunctions[node][1])

                    for conn in conjunctions[node][1]:
                        if conn in conjunctions:
                            conjunctions[conn][0][node] = True
                # all high:
                else:
                    queue += [(False, conn) for conn in conjunctions[node][1]]

                    lows += len(conjunctions[node][1])

                    for conn in conjunctions[node][1]:
                        if conn in conjunctions:
                            conjunctions[conn][0][node] = False

        if button_presses == 1000:
            print(lows * highs)

    print(math.lcm(*[sent[1] - sent[0] for sent in high_signal_sent.values()]))


if __name__ == "__main__":
    main()