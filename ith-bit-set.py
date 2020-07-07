"""
Check if ith bit is set or not
SAMPLE INPUT 5, i=2
SAMPLE OUTPUT True
"""


class ibit:

    def __init__(self, num, i):
        self.num = num
        self.i = i

    def ith_bit_check(self):

        result = self.num & (1 << self.i)
        if result:
            print(True)
        else:
            print(False)


def main():
    m = ibit(5, 2)
    m.ith_bit_check()


if __name__ == '__main__':
    main()