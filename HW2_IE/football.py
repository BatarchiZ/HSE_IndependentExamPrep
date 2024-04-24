import sys

# file = open('input.txt')
n, m = map(int, sys.stdin.readline().split())

# gamesDiff = [0 for i in range(100001)]
playersStat = [0 for i in range(n)]
peopleWhoRBetter = 0
for z in range(m):
    goal1, goal2 = map(int, sys.stdin.readline().split())
    gamesDiff = goal1 - goal2

    listPlay = [int(x) for x in sys.stdin.readline().split()]
    listLose = listPlay[:5]
    listWin = listPlay[5:]
    for i in listLose:
        playersStat[i] += gamesDiff
    for i in listWin:
        playersStat[i] -= gamesDiff
    if 0 in listLose or 0 in listWin:
            peopleWhoRBetter = 0
            for i in range(len(playersStat)):
                if playersStat[i] > playersStat[0]:
                    peopleWhoRBetter += 1
    else:
        for x in listPlay: # Tut nado raznye cases rassmotret'
            if playersStat[x] - abs(gamesDiff) <= playersStat[0] and playersStat[x] > playersStat[0]:
                peopleWhoRBetter += 1
            if playersStat[x] + abs(gamesDiff) > playersStat[0] and playersStat[x] <= playersStat[0]:
                peopleWhoRBetter -= 1
        # for x in listWin:
        #     if playersStat[x] - gamesDiff <= playersStat[0] and playersStat[x] > playersStat[0]:
        #         peopleWhoRBetter += 1
        # for x in listLose:
        #     if playersStat[x] + gamesDiff > playersStat[0] and playersStat[x] <= playersStat[0]:
        #         peopleWhoRBetter -= 1
    print(peopleWhoRBetter)

# print(playersStat)
