"""
In the world of dragon ball, Goku has been the greatest rival of Vegeta.
Vegeta wants to surpass goku but never succeeds. Now that he knows he cant beat goku in physical strength,
he wants to be satisfied by beating goku in mental strength. He gives certain inputs and outputs ,
Goku needs to find the logic and predict the output for the next inputs. Goku is struggling with the challenge,
your task is to find the logic and and help him win the challenge.
SAMPLE INPUT 0,1,5,12,22,1424
SAMPLE OUTPUT 0,1,2,2,3,4
"""

class mystery:

    def __init__(self, num):
        self.num = num
        self.result = ""


    def convertBinary(self, num):
        if num > 1:
            self.convertBinary(num // 2)

        self.result += str(num % 2)
        return self.result

    def goku_victory(self):
        binary_form = self.convertBinary(self.num)
        count = 0
        for i in binary_form:
            if i == '1':
                count += 1
        return count


def main():
    m = mystery(1424)
    print(m.goku_victory())


if __name__ == '__main__':
    main()