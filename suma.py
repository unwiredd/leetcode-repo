#!/sbin/python

d = 0
rs = 0
x = 0 ##pieniądze
tyg = d // 7
rest = d % 7
pn = 1
wt = 2
sr = 3
cz = 4
pt = 5
sb = 6
nd = 7
    
def tydzien():
    global tyg, pn, wt, sr, cz, pt, sb, nd, x
    while tyg > 0:
        sum = pn + wt + sr + cz + pt + sb + nd
        pn = pn + 1
        wt = wt + 1
        sr = sr + 1
        cz = cz + 1
        pt = pt + 1
        sb = sb + 1
        nd = nd + 1
        x = x + sum
        print(f"x: {x}")
        tyg = tyg - 1

def reszta():
    global tyg, pn, wt, sr, cz, pt, sb, nd, rest, rs
    if rest == 1:
        rs = pn
    elif rest == 2:
        rs = pn + wt
    elif rest == 3:
        rs = pn + wt + sr
    elif rest == 4:
        rs = pn + wt + sr + cz
    elif rest == 5:
        rs = pn + wt + sr + cz + pt
    elif rest == 6:
        rs = pn + wt + sr + cz + pt + sb
    elif rest == 7:
        rs = pn + wt + sr + cz + pt + sb
            
def totalMoney(n):
    """
    :type n: int
    :rtype: int
    """
    global d, tyg, rest
    d = n
    tyg = d // 7
    rest = d % 7
    print(f"rest: {rest}")
    tydzien()
    reszta()
    return (x + rs)

suma = totalMoney(20)
print(f"suma: {suma}")

