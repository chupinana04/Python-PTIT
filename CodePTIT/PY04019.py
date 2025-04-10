def chuanHoa(s):
    s = float(s)
    if s > 10:
        return s / 10.0
    return s
class ThiSinh:
    def __init__(self, id, ten, lt, th):
        self.id = "TS0" + str(id)
        self.ten = ten
        self.lt = chuanHoa(lt)
        self.th = chuanHoa(th)
        self.diemTB = (self.lt + self.th) / 2
        self.xepLoai = self.tinhXepLoai()
    def tinhXepLoai(self):
        if self.diemTB > 9.5:    return "XUAT SAC"
        elif self.diemTB >= 8:   return "DAT"
        elif self.diemTB >= 5:   return "CAN NHAC"
        return "TRUOT"
    def __str__(self):
        return self.id  + " " + self.ten + " " + "{:.2f}".format(self.diemTB) + " " + self.xepLoai
if __name__ == "__main__":
    listTS = []
    for t in range(int(input())):
        listTS.append(ThiSinh(t + 1, input(), input(), input()))
    listTS = sorted(listTS, key = lambda ts : ts.diemTB, reverse=True)
    for ts in listTS:
        print(ts)