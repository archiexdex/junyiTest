

if __name__ == "__main__": 
    n = int(input("input: "))
    cnt = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            cnt += 1
        elif i % 3 == 0 or i % 5 == 0:
            pass
        else:
            cnt += 1
    print("output:", cnt)
