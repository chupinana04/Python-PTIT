from collections import Counter


def change(s):
    tmp = [int(i) for i in s.split(":")]
    return tmp[0] * 60 + tmp[1]
class TramDo:
    def __init__(self, id, ten, bd, kt, mua):
        self.id = 'T' + '%02d' %id
        self.ten = ten
        self.bd = bd
        self.kt = kt
        self.mua = mua
        self.tgian = change(kt) - change(bd)
    def setTG(self, x, y):
        self.tgian += (change(y) - change(x))
    def setMua(self, x):
        self.mua += x

    def __str__(self):
        return self.id + " "  + self.ten + " " + '{:.2f}'.format(self.mua / self.tgian * 60)
if __name__ == "__main__":
    listTD = []
    cnt = 1
    for t in range(int(input())):
        ten = input()
        ok = 0
        for i in listTD:
            if i.ten == ten:
                i.setTG(input(), input())
                i.setMua(int(input()))
                ok = 1
        if ok == 0:
            listTD.append(TramDo(cnt, ten, input(), input(), int(input())))
            cnt += 1
    for tramDo in listTD:
        print(tramDo)


