from decimal import *
class HocSinh:
    def __init__(self, id, ten, data):
        self.id = "HS" + "{:02d}".format(id)
        self.ten = ten
        self.diemTB = (sum(float(x) for x in data) + data[0] + data[1])
        self.xepLoai = self.xetXepLoai()
    def xetXepLoai(self):
        self.diemTB = round(self.diemTB / 10 / 1.2, 1)
        if self.diemTB >= 9:
            return "XUAT SAC"
        elif self.diemTB >= 8:
            return "GIOI"
        elif self.diemTB >= 7:
            return "KHA"
        elif self.diemTB >= 5:
            return "TB"
        return "YEU"
    def __str__(self):
        return self.id + " " + self.ten + " " + '{:.1f}'.format(self.diemTB) + " " + self.xepLoai
if __name__ == "__main__":
    listHS = []
    for t in range(int(input())):
        ten = input()
        arr = [float(x) for x in input().split()]
        listHS.append(HocSinh(t + 1, ten, arr))
    listHS = sorted(listHS, key = lambda hs : hs.diemTB, reverse=True)
    for hs in listHS:
        print(hs)