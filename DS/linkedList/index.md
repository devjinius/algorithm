# 링크드 리스트

이미 알고있는 지식이지만 막상 구현하라고 하면 망설여진다. 이번 기회에 마스터 해보자.

링크드 리스트는 커밋의 구조를 생각하면 좋을 것 같다. 커밋은 항상 부모의 노드를 가리키며 연결된다. 링크드리스트 역시 자신의 다음 링크를 가리킨다.

## 싱글 링크드 리스트

단방향을 생각하면 쉽다. next 노드만 알고있고 자신을 참조하는 이전 노드는 모른다.

## 더블 링크드 리스트

양방향이다. next와 prev 노드의 참조값을 모두 가지고 있다.

## 서큘라 더블 링크드 리스트

기본 구조는 양방향이다. 다만 마지막 노드의 next값이 첫번째 노드이다. 동시에 첫번째 노드의 prev값이 마지막 노드가 된다.

즉 끝과 처음을 연결해 원을 그리는 구조다.

## 센티넬이란?

센티넬은 끝 노드를 말한다. 말단이라고 생각하면 좋겠다. 트리구조에서도 자식이 없는 마지막 노드가 센티널이 된다.