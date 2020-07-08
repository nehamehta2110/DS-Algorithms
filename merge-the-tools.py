"""
Sample Input: AABCAAADA 3
Sample Output: AB CA AD
Explanation: String s is split into total-length/3 equal parts of length 3. we output by
removing any subsequent occurrences of non-distinct characters
"""


def merge_the_tools(string, k):

    t = len(string)
    total = t//k
    for i in range(total):
        s = string[(3*i):(3*(i + 1))]
        dic = {}

        for j in range(len(s)):
            if s[j] not in dic.keys():
                dic[s[j]] = 1

            else:
                dic[s[j]] += 1

        print("".join(dic.keys()))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)