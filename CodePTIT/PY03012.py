class student:
    def __init__(self, hoVaTen, soBaiLamDung, soLanNop):
        self.hoVaTen = hoVaTen
        self.soBaiLamDung = soBaiLamDung
        self.soLanNop = soLanNop
    def __repr__(self):
        return "{} {} {}".format(self.hoVaTen, self.soBaiLamDung, self.soLanNop)
def sort_student(list_HS):
    return sorted(list_HS, key = lambda hs: (-hs.soBaiLamDung, hs.soLanNop, hs.hoVaTen))
if __name__ == "__main__":
    n = int(input())
    list_HS = []
    for _ in range(n):
        hoVaTen = input().strip()
        soBaiLamDung, soLanNop = map(int, input().split())
        list_HS.append(student(hoVaTen, soBaiLamDung, soLanNop))
    sorted_student = sort_student(list_HS)
    for student in sorted_student:
        print(student)