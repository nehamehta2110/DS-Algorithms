"""Consider a number N and you need to find if N is a power of 2. """


def isPower(num):
    if num == 0:
        return False
    else:
        while num % 2 == 0:
            return True
        return False


def main():
    print(isPower(5))


if __name__ == '__main__':
    main()
