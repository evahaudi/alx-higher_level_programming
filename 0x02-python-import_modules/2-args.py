#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    userin = argv[1:]
    num_args = len(userin)
    print("{:d} {:s}{:s}".
          format(num_args,
                 "arguments" if (num_args) != 1 else "argument",
                 "." if (num_args) == 0 else ":"))
    for idx, arg in enumerate(userin):
        print("{:d}: {:s}".format(idx + 1, arg))
