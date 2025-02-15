if __name__ == '__main__':
    for t in range(int(input())):
        s1 = input()
        s2 = input()
        i = s1.find(s2)
        cnt = 0
        if i == -1:
            cnt = 0
        else:
            while i != -1:
                i = s1.find(s2)
                #print(i)
                s1 = s1[:i] + s1[i + len(s2):]
                cnt += 1
            cnt -= 1
        print(cnt)
