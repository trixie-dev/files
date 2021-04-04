# coding: utf8
while True:
    t = True
    l=[]
    while t:
        a=list(map(str, input().split('.')))
        l.append(a)
        if a[0]=='':
            t=False
    l.remove(l[-1])






    print(l)
