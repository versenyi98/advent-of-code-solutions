import sys
lines = sys.stdin.read().split("\n")

register = 1
signal_strength = 0
cycle = 0
sprites = []

for line in lines:
    value = 0
    cycles_to_run = 1

    if line != 'noop':
        value = int(line.split()[-1])
        cycles_to_run = 2

    while cycles_to_run:
        cycles_to_run -= 1

        if cycle % 40 == 19:
            signal_strength += register * (cycle + 1)
        if cycle % 40 == 0:
            sprites += [""]
        sprite_pos = cycle % 40
        sprites[-1] += "#" if sprite_pos - 1 <= register <= sprite_pos + 1 else "."
        cycle += 1

    register += value

print(signal_strength)

# there are 8 digits displayed in the sprite
for sprite in sprites:
    print(sprite)