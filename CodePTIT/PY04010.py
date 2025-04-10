class ThiSinh:
    def __init__(self, hoTen, ngaySinh, diem1, diem2, diem3):
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tongDiem = diem1 + diem2 + diem3
    def __str__(self):
        return f'{self.hoTen} {self.ngaySinh} {self.tongDiem:.1f}'
if __name__ == "__main__":
    ts = ThiSinh(input().strip(), input().strip(), float(input()), float(input()), float(input()))
    print(ts)