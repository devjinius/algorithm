def solution(skill, skill_trees):
    skills = list(skill)
    count = 0
    for skill_tree in skill_trees:
        curSkill = 0
        isBreak = False
        for skill in skills:
            if (skill == skills[0]):
                curSkill = skill_tree.find(skill)
                continue

            nextSkill = skill_tree.find(skill)
            if (curSkill == -1 and nextSkill != -1):
                isBreak = True
                break
            if (nextSkill != -1 and curSkill > nextSkill):
                isBreak = True
                break
            curSkill = nextSkill

        if(not isBreak):
            count += 1

    print(count)


# solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA', 'CD'])
# solution('XDC', ['BDA'])
# solution('YDZ', ['YACDZ', 'CZADF', 'YAEDCBZ', 'YBDA'])
# solution('ABCDEZ', ['ZA', 'AZ'])
# solution('ABC', ['AZC'])
solution('ZDFP', ['ZD', 'ZC', 'DF', 'ZADBCF', 'ABC'])
