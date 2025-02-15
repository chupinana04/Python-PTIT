def convert(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while n > 0:
        result = digits[n % b] + result
        n //= b
    return result
if __name__ == "__main__":
    for t in range(int(input())):
        n, b = map(int, input().split())
        print(convert(n, b))
