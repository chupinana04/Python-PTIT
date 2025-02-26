from math import sqrt


class Point:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def distance(self, k):
        x0 = self.tu - k.tu
        y0 = self.mau - k.mau
        return sqrt(x0 * x0 + y0 * y0)
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def chuVi(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if max(a, b, c) * 2 >= a + b + c:
            return "INVALID"
        else:
            return "{:.3f}".format(a + b + c)

if __name__ == "__main__":
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        triangle = Triangle(Point(a[i], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
        print(triangle.chuVi())
        i += 6
