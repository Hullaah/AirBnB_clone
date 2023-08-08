def parse_arg(arg: str) -> list:
    args = []
    while True:
        first = arg.find('"')
        second = arg[first + 1:].find('"')
        second = second if second == -1 else second + first + 1
        if first == -1 or second == -1:
            args.extend(arg.split())
            break
        else:
            try:
                if arg[first - 1] == " ":
                    args.extend(arg[0:first].split())
                    args.extend([arg[first:second + 1]])
                else:
                    args.extend(arg[0:second + 1].split())
            except IndexError:
                args.extend(arg[0:first].split())
                args.extend([arg[first:second + 1]])
        arg = arg[second + 1:]
    return args

print(parse_arg('Hello bola how "are you" girl "I will be "there right now'))
print(parse_arg('Hello bola how are you girl I will "be there right now'))
print(parse_arg('Hello bola how are you girl I will because"be" there right now'))
print(parse_arg('Hi"Hello "bola how are you girl I will be there right now'))
