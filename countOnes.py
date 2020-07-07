"""
Count number of ones in binary representation of a number with O(k) complexity where k is number of ones
SAMPLE INPUT 23
SAMPLE OUTPUT 4
"""


class counting:

    def __init__(self, num):
        self.num = num
        self.result = ""

    def total_ones(self):
        count = 0
        while(self.num):
            self.num = (self.num) & (self.num - 1)
            count +=1
        print(count)


def main():
    m = counting(23)
    m.total_ones()


if __name__ == '__main__':
    main()