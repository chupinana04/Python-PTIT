def doiVePhut(tg):
    h, m = map(int, tg.split(":"))
    return h * 60 + m
def chuanHoa(tg):
    return f"{tg//60} gio {tg % 60} phut"
class NguoiChoi:
    def __init__(self, ma, ten, gioVao, gioRa):
        self.ma = ma
        self.ten = ten
        self.gioVao = doiVePhut(gioVao)
        self.gioRa = doiVePhut(gioRa)
        self.tg = self.gioRa - self.gioVao
    def __str__(self):
        return f"{self.ma} {self.ten} {chuanHoa(self.tg)}"
if __name__ == "__main__":
    listNC = []
    for t in range(int(input())):
        listNC.append(NguoiChoi(input(), input(), input(), input()))
    listNC = sorted(listNC, key=lambda nc : -nc.tg)
    for nc in listNC:
        print(nc)