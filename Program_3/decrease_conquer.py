
def supermode_decrease(list, extra = None):

    n = len(list)
    if n == 0:
        return extra
    tups_list = []
    if n % 2 == 1:
        extra = list[-1]
    for i in range(0, n-1, 2):
        if list[i] == list[i+1]:
            tups_list.append(list[i])
    supermode = supermode_decrease(tups_list, extra )
    if supermode is None:
        return "No mode"
    supermode_count = list.count(supermode)
    if supermode_count > n/2:
        return supermode
    if supermode_count == n/2 and supermode == extra:
       return supermode
    return "No mode"




arr = [3, 2, 4, 3, 4, 4, 2, 4, 4]
arr2 = [3, 2, 4, 3, 4, 4, 2, 4]
arr4 = [3, 2, 4, 3, 4, 4, 2, 4, 3, 3, 3, 3, 3]
arr5 = [1, 1, 1, 1, 8, 8, 8, 8, 8]
arr6 = [1, 1, 1, 8, 8, 8, 8, 8]
arr7 = [4,3,4,2,4,1,4]
arr8 = [4,3,4,2,4,1,4,4]
arr9 = [4,3,4,2,4,1,2]
arr10 = [8, 8, 8, 8, 8, 1, 1, 1, 1]
arr11 = [2,2,2,2,2]

print(supermode_decrease(arr))
print(supermode_decrease(arr2))
print(supermode_decrease(arr4))
print(supermode_decrease(arr5))
print(supermode_decrease(arr6))
print(supermode_decrease(arr7))
print(supermode_decrease(arr8))
print(supermode_decrease(arr9))
print(supermode_decrease(arr10))
print(supermode_decrease(arr11))
