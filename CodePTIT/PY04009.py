class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def cong(self, k):
        a = self.thuc + k.thuc
        b =self.ao + k.ao
        return SoPhuc(a, b)
    def nhan(self, k):
        a = self.thuc * k.thuc - self.ao * k.ao
        b = self.thuc * k.ao + self.ao * k.thuc
        return SoPhuc(a, b)
    def __str__(self):
        if self.ao < 0:
            return f'{self.thuc} - {abs(self.ao)}i'
        return f'{self.thuc} + {self.ao}i'
if __name__ == "__main__":
    for t in range(int(input())):
        arr = []
        while len(arr) < 4:
            arr += [int(i) for i in input().split()]
        a, b = SoPhuc(arr[0], arr[1]), SoPhuc(arr[2],arr[3])
        c = (a.cong(b)).nhan(a)
        d = (a.cong(b)).nhan(a.cong(b))
        print(c, d, sep = ", ")
