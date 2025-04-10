if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        my_set = set()
        for i in range(n):
            my_set.add(int(input()))
        if(len(my_set) == 1):   print("BANG NHAU")
        else:
            my_list = sorted(list(my_set))
            print(my_list[0], my_list[-1])
