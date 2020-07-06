""""
Ankit is in maze. The command center sent him a string which decodes to come out from the maze.
He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down.
In each command he will traverse 1 unit distance in the respective direction.
"""


def emazin(command):
    x1 = 0
    y1 = 0

    for i in command:
        if i == 'L':
            x1 -= 1

        elif i == 'R':
            x1 += 1

        elif i == 'D':
            y1 -= 1

        elif i == 'U':
            y1 += 1

    result = str(x1) + " " + str(y1)

    print(result)


def main():
    command = str(input())
    emazin(command)


if __name__ == "__main__":
    main()
