import math


class PhanSo:
    def __init__(self, tuSo, mauSo):
        x = math.gcd(tuSo, mauSo)
        self.tuSo = int(tuSo / x)
        self.mauSo = int(mauSo / x)
    def output(self):
        print(f"{self.tuSo}/{self.mauSo}")
if __name__ == "__main__":
    a, b = map(int, input().split())
    p = PhanSo(a, b)
    p.output()