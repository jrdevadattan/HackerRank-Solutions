def climbingLeaderboard(ranked, player):
    s = sorted(list(dict.fromkeys(ranked)), reverse=True)
    r = []
    a = len(s) - 1 
    for i in player:
        while a >= 0 and i >= s[a]:
            a -= 1
        r.append(a + 2)
    return r

if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    for i in result:
        print(i)
