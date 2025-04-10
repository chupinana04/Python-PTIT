def solve(s1, s2):
    arr1 = sorted(list(s1))
    arr2 = sorted(list(s2))
    if(arr1 == arr2):
        return "YES"
    return "NO"
if __name__ == "__main__":
    for t in range(int(input())):
        s1, s2 =input(), input()
        print("Test " + str(t + 1) + ": " + solve(s1, s2))