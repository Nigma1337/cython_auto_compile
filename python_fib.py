if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='fib lol')
    parser.add_argument("thing", metavar='F', type=str, help='file to run compilation on')
    args = parser.parse_args()
    n = 1000
    """Print the Fibonacci series up to n."""
    a = 0
    b = 1
    while b < n:
        a, b = b, a + b
    if args.thing == "e":
        a = "e"

for i in [s for s in dir() if not '__' in s]: print(i, eval('type(%s)'%i))