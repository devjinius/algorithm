# 백준알고리즘 1991
# https://www.acmicpc.net/problem/1991

# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
# 예를 들어 위와 같은 이진 트리가 입력되면,

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

nodeLen = int(input())
nodeList = [None] * 26


class Node:
    def __init__(self, name, left, right):
        self.name = name
        if left == '.':
            self.left = None
        else:
            self.left = ord(left)-65
        if right == '.':
            self.right = None
        else:
            self.right = ord(right)-65


for _ in range(nodeLen):
    name, left, right = input().split(" ")
    nodeList[ord(name)-65] = Node(name, left, right)


def preOrder(node, nodeList):
    if node == None:
        return
    print(nodeList[node].name, end='')
    preOrder(nodeList[node].left, nodeList)
    preOrder(nodeList[node].right, nodeList)


def inOrder(node, nodeList):
    if node == None:
        return
    inOrder(nodeList[node].left, nodeList)
    print(nodeList[node].name, end='')
    inOrder(nodeList[node].right, nodeList)


def postOrder(node, nodeList):
    if node == None:
        return
    postOrder(nodeList[node].left, nodeList)
    postOrder(nodeList[node].right, nodeList)
    print(nodeList[node].name, end='')


preOrder(0, nodeList)
print()
inOrder(0, nodeList)
print()
postOrder(0, nodeList)
print()
