#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    count = len(sys.argv) - 1
    for i in range(count):
        int_value = int(sys.argv[i + 1])
        result += int_value
    print("{}".format(result))
