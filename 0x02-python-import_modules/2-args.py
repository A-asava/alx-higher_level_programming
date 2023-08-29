#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len_count = len(sys.argv) - 1
    if len_count == 0:
        print("0 arguments.")
    elif len_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_count))
    for i in range(len_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
