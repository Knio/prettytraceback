import sys
print('\n'.join(sys.path))

import prettytraceback

def error():
    x = 1/0

if __name__ == '__main__':
    error()

