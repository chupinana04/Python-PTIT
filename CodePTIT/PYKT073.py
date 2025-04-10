if __name__ == "__main__":
    cnt = 0
    result = []
    line = []
    len_list = ""
    for t in range(int(input())):
        line.append(list([str(s) for s in input().split()]))
    for i in line:
        len_list += str(len(i))
    len_list = len_list.replace("7777", "2").replace("68", "1")
    while "11" in len_list:
        len_list = len_list.replace("11", "1")
    print(len(len_list))
    for i in len_list:
        print(i)
