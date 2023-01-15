testcase1 = [1, 2, 3, 4, 5]
testcase2 = [5, 4, 3, 2, 1]
testcase3 = [1, 3, 2, 7, 88, 0]


def merge(l, r):
    result = []
    r_idx, l_idx = 0, 0
    while l_idx < len(l) and r_idx < len(r):
        if l[l_idx] <= r[r_idx]:
            result.append(l[l_idx])
            l_idx += 1
        else:
            result.append(r[r_idx])
            r_idx += 1
    if l:
        result.extend(l[l_idx:])
    if r:
        result.extend(r[r_idx:])
    return result


def mergesort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = mergesort(left)
    right = mergesort(right)
    return list(merge(left, right))


print(mergesort(testcase1))
print(mergesort(testcase2))
print(mergesort(testcase3))
