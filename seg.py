for _ in range(int(input())):
    n = int(input())
    d = {}
    a = 0
    for i in range(n):
        l, r, v = map(int, input().split())
        if v in d.keys():
            b = 0
            for (x,y) in d[v].keys():
                if (x>=l and x<=r) or (y>=l and y<=r):
                    d[v][(x,y)] += 1
                    b = 1
                if d[v][(x,y)] > 2:
                    a = 1
            if b == 1:
                d[v][(l,r)] = 1
            else:
                d[v][(l,r)] = 0
        else:
            d[v] = {(l,r):0}
    if a == 0:
        print('YES')
    else:
        print('NO')