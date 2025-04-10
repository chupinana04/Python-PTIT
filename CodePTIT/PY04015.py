class KhachHang:
    def __init__(self, id, ten, cu, moi):
        self.id = "KH" + "{:02d}".format(id)
        self.ten = ten
        self.moi = moi
        self.cu = cu
        self.so = self.moi - self.cu
        self.phuPhi = self.tinhPhuPhi()
        self.tongTien = self.tinhTongTien() * (1 + self.phuPhi)
    def tinhPhuPhi(self):
        x = self.so
        if x > 100: return 0.05
        elif x >= 51:   return 0.03
        return 0.02
    def tinhTongTien(self):
        x = self.so
        if x > 100: return 100 * 50 + 50 * 150 + (x - 100) * 200
        elif x >= 51: return 100 * 50 + (x - 50) * 150
        return 100 * x
    def __str__(self):
        return self.id + " " + self.ten + " " + str(round(self.tongTien))
if __name__ == "__main__":
    listKH = []
    for t in range(int(input())):
        listKH.append(KhachHang(t + 1, input(), int(input()), int(input())))
    listKH = sorted(listKH, key = lambda kh : kh.tongTien, reverse=True)
    for kh in listKH:
        print(kh)