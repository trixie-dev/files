def subsequence(seq: list) -> list:
    for el in seq: new = filter(lambda el: _dividers(el) <= 4, seq)
    it = iter(new)
    for el in it: print(next(it))



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

#for el in filter(None, range(5): print(el, end=' ')


seq = [4, 6, 7, 9, 10, 10, 5, 4, 4, 16, 22]

subsequence(seq)
'''
1. c
2. d
3. a
4. e
5. b
'''

