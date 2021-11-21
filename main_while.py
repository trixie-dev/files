n = int(input())
for _ in range(0, n):
    
    seq = tuple(input())
    def subsequence(seq: tuple) -> list:
        for el in seq: new = filter(lambda el: _dividers(el) <= 4, seq)
        l_new = list(new)
        start = []
        end = []
        for i in range(1, len(l_new)): 
            if l_new[i-1] < l_new[i]:
                i2 = i + 1
                while i2 < len(l_new) and l_new[i2 - 1] <= l_new[i2]:
                    i2 += 1
                if i2 != i + 1:
                    while i2 < len(l_new) and l_new[i2 - 1] >= l_new[i2]:
                        i2 += 1
                    start.append(i - 1)
                    end.append(i2) 
        
        if len(start) != 0 and len(end) != 0: 
            l_out = l_new[start[0]: end[0]]
        else: 
            l_out = []
        return l_out


    def _dividers(n: int) -> int:
        i = 1
        a = []
        while i * i <= n:
            if n % i == 0:
                a.append(i)
                if i != n // i:
                    a.append(n // i)
            i += 1
        return len(a)


    print(subsequence(seq))

    # 4, 6, 7, 9, 10, 10, 5, 4, 4
