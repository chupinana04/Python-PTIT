class Rectangle:
    def __init__(self, cDai, cRong, mSac):
        self.cDai = cDai
        self.cRong = cRong
        self.mSac = mSac[0:1:].upper() + mSac[1::].lower()
    def perimeter(self):
        return (self.cDai + self.cRong) * 2
    def area(self):
        return self.cDai * self.cRong
    def check(self):
        if self.cDai <= 0 or self.cRong <= 0:   return False
        return True
a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), a[2])
if rec.check():
    print(f"{rec.perimeter()} {rec.area()} {rec.mSac}")
else:
    print("INVALID")
