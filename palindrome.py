"""
You have been given a String S. You need to find and print whether this string is a palindrome or not.
If yes, print "YES" (without quotes), else print "NO" (without quotes).
Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.
Output Format
Print the required answer on a single line.
"""


def palindrome_string(s):
    s1 = ''
    for i in s[::-1]:
        s1 += i
    if s1 == s:
        print('YES')
    else:
        print('NO')


def main():
    s = str(input())
    palindrome_string(s)


if __name__ == '__main__':
    main()
