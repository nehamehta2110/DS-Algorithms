'''
You have been given a String S consisting of uppercase and
lowercase English alphabets. You need to change the case of each alphabet in this String.
That is, all the uppercase letters should be converted to lowercase and all the lowercase letters
should be converted to uppercase. You need to then print the resultant String to output.
Input Format
The first and only line of input contains the String S
Output Format
Print the resultant String on a single line.
'''


def toggleCase(S):
    S_result = ""
    for i in S:
        if i.islower():
            i = i.upper()
            S_result += i

        elif i.isupper():
            i = i.lower()
            S_result += i

    print(S_result)


def main():
    S = str(input())
    toggleCase(S)


if __name__ == "__main__":
    main()
