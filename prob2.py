for _ in range(int(input())):
    n = str(input())
    l = list(n)
    l1 = []
    for i in l:
        l1.append(int(i))
    if l1.count(0) == 0:
        l1.remove(max(l1))
    else:
        m = 0
        for i in range(len(l1)):
            if l1[i] != 0:
                if l1[i] > m:
                    m = l1[i]
            else:
                l1.remove(m)
                while l1[0] == 0:
                    l1.remove(l1[0])
                break
    print(*l1, sep='')