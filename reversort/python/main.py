def reversort(n, arr):
    cost = 0
    for i in range(n - 1):
        m = min(arr[i:])
        j = arr.index(m) + 1
        arr[i: j] = reversed(arr[i: j])
        cost += j - i
    return cost


if __name__ == '__main__':
    test_cases = int(input())
    for test_case in range(1, test_cases + 1):
        size = int(input())
        arr = list(map(int, input().split()))
        print(f"Case #{test_case}: {reversort(size, arr)}")
