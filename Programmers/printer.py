def solution(priorities, location):

    queue = [i for i in range(len(priorities))]
    target = queue[location]

    priorQueue = sorted(priorities, reverse=True)
    count = 0

    while(len(priorities) != 0):
        removeItem = priorities.pop(0)
        removeIndex = queue.pop(0)

        if removeItem == priorQueue[0]:
            count += 1
            priorQueue.pop(0)
            if removeIndex == target:
                return count
            continue

        priorities.append(removeItem)
        queue.append(removeIndex)

    # return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
