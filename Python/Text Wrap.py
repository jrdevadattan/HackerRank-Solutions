import textwrap

def wrap(string, max_width):
    l = textwrap.wrap(string, max_width)
    return '\n'.join(l)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
