from math import isqrt

def check_prime(n):
    if n < 2: return False
    for i in range(2, isqrt(n) +  1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        hang = list(map(int, input().split()))
        matrix.append(hang)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if check_prime(matrix[i][j]):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
            print(matrix[i][j], end = " ")
        print()


