
# Clay Pigeon Shooting
# https://www.codewars.com/kata/clay-pigeon-shooting/train/python

# Pete and his mate Phil are out in the countryside shooting clay pigeons with a shotgun - amazing fun.

# They decide to have a competition. 3 rounds, 2 shots each. Winner is the one with the most hits.

# Some of the clays have something attached to create lots of smoke when hit, guarenteed by the packaging to generate 'real excitement!' (genuinely this happened).
# None of the explosive things actually worked, but for this kata lets say they did.

# For each round you will receive the following format:

# [{P1:'XX', P2:'XO'}, true]

# That is an array containing an object and a boolean. Pl represents Pete, P2 represents Phil. X represents a hit and O represents a miss.
# If the boolean is true, any hit is worth 2. If it is false, any hit is worth 1.

# Find out who won. If it's Pete, return 'Pete Wins!'. If it is Phil, return 'Phil Wins!'. If the scores are equal, return 'Draw!'.

# Note that as there are three rounds, the actual input (x) will look something like this:

# 입력
# [[{P1:'XX', P2:'XO'}, true], [{P1:'OX', P2:'OO'}, false], [{P1:'XX', P2:'OX'}, true]]

# 반환값
# string

# 출력
# 없음

from collections import Counter


def shoot(results):
    pete = 0
    phil = 0
    p1 = 0
    p2 = 0
    for round in results:
        [board, score] = round
        p1 = Counter(board['P1'])['X']
        p2 = Counter(board['P2'])['X']
        if(score):
            pete += p1 * 2
            phil += p2 * 2
        else:
            pete += p1 * 1
            phil += p2 * 1
    if (pete > phil):
        return "Pete Wins!"
    if (pete < phil):
        return "Phil Wins!"
    if (pete == phil):
        return 'Draw!'
