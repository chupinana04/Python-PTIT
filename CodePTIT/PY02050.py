if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        st = []
        for i in range(n):
            while len(st) > 0 and arr[st[-1]] <= arr[i]:
                st.pop()
            if len(st) == 0: print(i + 1, end = " ")
            else: print(i - st[-1], end = " ")
            st.append(i)
        print()
