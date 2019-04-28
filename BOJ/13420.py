# BOJ 13420 문제
# https://www.acmicpc.net/problem/13420

# 문제

# 사칙연산은 덧셈, 뺄셈, 곱셈, 나눗셈으로 이루어져 있으며, 컴퓨터 프로그램에서 이를 표현하는 기호는 +, -, *, / 와 같다. 아래는 컴퓨터 프로그램에서 표현한 사칙 연산의 예제이다.

# 3 * 2 = 6

# 문제와 답이 주어졌을 때, 이를 계산하여 올바른 수식인지 계산하는 프로그램을 만들려고 한다. 만약 주어진 데이터가 3 * 2 = 6 이라면 정답으로, 3 * 2 = 7 이면 오답으로 채점을 하면 된다.
# 문제와 답이 주어졌을 때, 이를 채점하는 프로그램을 작성하시오.

# 입력값
# 4
# 3 * 2 = 6
# 11 + 11 = 11
# 7 - 9 = -2
# 3 * 0 = 0

# 출력값
# correct
# wrong answer
# correct
# correct

# ===========================================================================

import sys
testLen = int(input())

for _ in range(testLen):

    rightAnswer = 0
    [operand1, operator, operand2, equal, answer] = sys.stdin.readline().split(" ")

    if(operator == '+'):
        rightAnswer = int(operand1) + int(operand2)
    elif(operator == '-'):
        rightAnswer = int(operand1) - int(operand2)
    elif(operator == '*'):
        rightAnswer = int(operand1) * int(operand2)
    elif(operator == '/'):
        rightAnswer = int(operand1) // int(operand2)

    if(rightAnswer == int(answer)):
        sys.stdout.write('correct\n')
    else:
        sys.stdout.write('wrong answer\n')
