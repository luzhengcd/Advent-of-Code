import re

def parse_input(input_path = 'input.txt'):
    pattern = re.compile(r'(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    with open(input_path) as f:
        for line in f.readlines():
            reindeer, speed, fly_duration, rest_duration = re.match(pattern, line).groups()
            yield (reindeer, int(speed), int(fly_duration), int(rest_duration))

def main():
    reindeers = parse_input()
    answer = 0
    for _, speed, fly_duration, rest_duration in reindeers:
        n, remaining = divmod(2503, fly_duration + rest_duration)
        answer = max(answer, n * fly_duration * speed + min(remaining, fly_duration) * speed )
    print('Answer for part 1: ', answer)

if __name__ == '__main__':
    main()
