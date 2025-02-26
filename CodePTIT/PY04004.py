import math


class PhanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = tuSo
        self.mauSo = mauSo
    def rutGon(self):
        x = math.gcd(self.tuSo, self.mauSo)
        self.tuSo = int(self.tuSo / x)
        self.mauSo = int(self.mauSo / x)
    def cong(self, k):
        p = PhanSo(0, 0)
        p.tuSo = self.tuSo * k.mauSo + self.mauSo * k.tuSo
        p.mauSo = self.mauSo * k.mauSo
        p.rutGon()
        return p
    def output(self):
        print(f"{self.tuSo}/{self.mauSo}")
if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    p = PhanSo(a, b)
    q = PhanSo(c, d)
    s = q.cong(p)
    s.output()