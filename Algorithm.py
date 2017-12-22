def insertion_sort(v):
    for j in range(1, len(v)):
        key = v[j]
        i = j-1
        while i >= 0 and v[i] > key:
            v[i+1] = v[i]
            i = i-1
        v[i+1] = key


def quick_sort(v, p, r):
    if p < r:
        q = partition(v, p, r)
        quick_sort(v, p, q-1)
        quick_sort(v, q+1, r)


def partition(v, p, r):
    x = v[r]
    i = p-1
    for j in range(p, r):
        if v[j] <= x:
            i += 1
            v[i], v[j] = v[j], v[i]
    v[i+1], v[r] = v[r], v[i+1]
    return i+1


def best_quick_sort(v, p, r):
    if p < r:
        q = best_partition(v, p, r)
        best_quick_sort(v, p, q-1)
        best_quick_sort(v, q+1, r)


def best_partition(v, p, r):
    x = v[(p+r)//2]
    i = p-1
    for j in range(p, r):
        if v[j] <= x:
            i += 1
            v[i], v[j] = v[j], v[i]
    v[i+1], v[r] = v[r], v[i+1]
    return i+1