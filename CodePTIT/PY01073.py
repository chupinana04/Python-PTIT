from itertools import permutations

if __name__ == '__main__':
    s = input()
    for p in permutations(s):
        print("".join(p))
