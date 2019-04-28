# BOJ 13417 문제
# https://www.acmicpc.net/problem/13417

# 문제

# 문제
# N장의 카드가 일렬로 놓여있다. 각 카드에는 알파벳이 하나씩 적혀있다. 태욱이는 가장 왼쪽에 있는 카드부터 차례대로 한 장씩 가져올 수 있다. 가장 처음에 가져온 카드는 자신의 앞에 놓는다.
# 그다음부터는 가져온 카드를 자신의 앞에 놓인 카드들의 가장 왼쪽, 또는 가장 오른쪽에 놓는다. 태욱이는 모든 카드를 다 가져온 후에 자신의 앞에 놓인 카드를 순서대로 이어 붙여 카드 문자열을 만들려고 한다.

# 예를 들어 3장의 카드가 [M, K, U] 순으로 놓여있다고 하자. 태욱이는 먼저 가장 왼쪽에 있는 “M”이 적힌 카드를 가져와서 자신의 앞에 놓는다.
# 다음으로 남은 카드 중 가장 왼쪽에 있는 “K”가 적힌 카드를 가져와서 가장 왼쪽에 두고, 이어서 “U”가 적힌 카드를 가져와서 다시 가장 왼쪽에 두면 “UKM”이라는 문자열을 만들 수 있다.
# 만약 “K”가 적힌 카드를 가져와서 가장 왼쪽에 두고, 이어서 “U”가 적힌 카드를 가져와서가장 오른쪽에 두면 “KMU”라는 문자열을 만들 수 있다.
# 이때, 태욱이가 만들 수 있는 문자열 중 사전 순으로 가장 빠른 문자열은 “KMU”이다.

# N장의 카드에 적혀있는 알파벳의 처음 순서가 주어질 때, 태욱이가 만들 수 있는 카드 문자열 중 사전 순으로 가장 빠른 문자열을 출력하는 프로그램을 작성하시오.

# 입력값
# 3
# 3
# M K U
# 5
# A S D F G
# 7
# B A C A B A C

# 출력값
# KMU
# ASDFG
# AAABCBC

# ===========================================================================

import sys
testLen = int(input())

for _ in range(testLen):

    inputListLen = int(sys.stdin.readline())
    inputList = sys.stdin.readline().rstrip('\n').split(" ")
    answerList = []
    firstWord = ''

    for i in inputList:
        if (len(answerList) == 0):
            answerList.append(i)
            firstWord = i
        else:
            if (firstWord < i):
                answerList.append(i)
            else:
                answerList.insert(0, i)
                firstWord = i
    answerStr = "".join(answerList) + '\n'
    sys.stdout.write(answerStr)
