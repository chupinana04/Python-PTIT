import random
class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.trangThai = ""
    def cap_nhat(self, s):
        for i in s:
            if i == 'v':    self.diem -= 2
            if i == 'm':    self.diem -= 1
        if self.diem <= 0:
            self.diem = 0
            self.trangThai = "KDDK"
    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop} {self.diem} {self.trangThai}"
if __name__ == "__main__":
    n = int(input())
    list_sv = []
    for i in range(n):
        sv = SinhVien(input(), input(), input())
        list_sv.append(sv)
    for i in range(n):
        ma_sv, s = map(str, input().split())
        for sv in list_sv:
            if sv.ma == ma_sv:
                sv.cap_nhat(s)
    for sv in list_sv:
        print(sv.__str__())




