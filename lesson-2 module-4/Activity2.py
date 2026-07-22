tuplex=(1,2,3,3,2,1)
def palaindrom(r):
    e=len(r)-1
    s=0
    while s<e:
        if(r[s]!=r[e]):
            return False
        s=s+1
        e=e-1
    return True
if palaindrom(tuplex):
    print("tuplex is flipflop")
else:
    print("tuplex is not flipflop")