"""
Given a input integer, output the binary representation of the number
"""
def convertBinary(num):

    if num>1:
        convertBinary(num // 2)

    print(num % 2, end='')

def main():
    convertBinary(1424)


if __name__ == '__main__':
    main()
