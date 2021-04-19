def color(text: str, code: int, bold: bool = False):
    prefix = ''
    if bold:
        prefix += '\033[1m'
    prefix += f'\033[{code}m'
    return prefix + text + '\033[0m'


def red(text, bold=False):
    return color(text, 31, bold)


def green(text, bold=False):
    return color(text, 32, bold)


if __name__ == '__main__':
    print(green('success'))
    print(red('failure'))
