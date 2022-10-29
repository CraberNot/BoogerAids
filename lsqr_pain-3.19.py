def lsqr(lst):
    n = len(lst)
    i = 0
    sqr = []
    while i < n:
    
        x = lst[i]
        sqr = sqr + [x**2]
        i = i + 1
    return sqr
print(lsqr([1,2,3,4]))
