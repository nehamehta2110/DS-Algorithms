"""
You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively.
The input word is considered similar to word zoo if . Determine if the entered word is similar to word zoo.
For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo
 and zzzooooo.
Input format
First line: A word that starts with several Zs and continues by several Os.
Output format
Print Yes if the input word can be considered as the string zoo otherwise, print No.
"""


def checkSimilar(string):
    match = 'zoo'
    dic = {}
    for i in match:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    dic2 = {}
    for j in string:
        if j in dic2.keys():
            dic2[j] += 1
        else:
            dic2[j] = 1

    for n in range(1, 7):
        if list(dic.values())[0] * n == list(dic2.values())[0] and list(dic.values())[1] * n == list(dic2.values())[1]:
            return 'Yes'
    return 'No'


def main():
    string = str(input())
    print(checkSimilar(string))


if __name__ == '__main__':
    main()
